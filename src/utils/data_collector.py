from os import getenv
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pandas import DataFrame, concat, read_csv
from dotenv import load_dotenv
from sodapy import Socrata

from utils import helpers

DOMAIN = "data.cityofnewyork.us"
CSV_FILE_PATH = "../../data/raw/"

load_dotenv(dotenv_path="../../.env")
app_token = getenv("SOCRATA_TOKEN")


class DataCollector:
    def __init__(self, endpoint="", filters=[], columns=[], date_col=""):
        self.endpoint = endpoint
        self.filters = filters
        self.columns = columns
        self.date_col = date_col
        self.client = Socrata(domain=DOMAIN, app_token=app_token, timeout=10)
        self.df = DataFrame()

    def _collect_data_for_year(self, year) -> DataFrame:
        query = self.filters + helpers.create_yearly_query(year, self.date_col)
        query = " AND ".join(query)
        select_str = ", ".join(self.columns) if self.columns else "*"
        dfs = []
        limit = 5000
        offset = 0

        while True:
            page_results = self.client.get(
                self.endpoint,
                where=query,
                select=select_str,
                limit=limit,
                offset=offset,
            )
            if not page_results:
                break
            print(f"{year} - {offset} records", flush=True)
            dfs.append(DataFrame(page_results))
            offset += limit

        return concat(dfs, ignore_index=True)

    def collect_data(self, years=[]) -> None:
        start = time.time()
        with ThreadPoolExecutor(max_workers=len(years)) as executor:
            future_to_year = {
                executor.submit(self._collect_data_for_year, year): year
                for year in years
            }
            dfs = []
            for future in as_completed(future_to_year):
                year = future_to_year[future]
                try:
                    df = future.result()
                    dfs.append(df)
                except Exception as error:
                    print(f"{year} generated an exception: {error}")

        self.df = concat(dfs, ignore_index=True) if dfs else DataFrame()
        end = time.time()
        print(
            f"""
            File size: {helpers.compute_filesize(self.df)} MB
            Operation took {end- start} seconds
            """
        )

    def read_data(self, name) -> None:
        file_path = CSV_FILE_PATH + name + ".csv"
        self.df = read_csv(file_path)

    def to_csv(self, file_name) -> None:
        self.df.to_csv(CSV_FILE_PATH + file_name, index=False)
