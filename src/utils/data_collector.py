from os import getenv
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pandas import DataFrame, concat
from dotenv import load_dotenv
from sodapy import Socrata

from utils import helpers
from utils.constants import Paths, Urls


class DataCollector:
    def __init__(self, endpoint="", filters=[], columns=[], date_col=""):
        self.endpoint = endpoint
        self.filters = filters
        self.columns = columns
        self.date_col = date_col

        load_dotenv(dotenv_path=Paths.ROOT_PATH / ".env")
        app_token = getenv("SOCRATA_TOKEN")

        self.client = Socrata(
            domain=Urls.OPEN_DATA_URL, app_token=app_token, timeout=10
        )
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

    def collect_data(self, year_range) -> None:
        start = time.time()
        with ThreadPoolExecutor(max_workers=len(year_range)) as executor:
            future_to_year = {
                executor.submit(self._collect_data_for_year, year): year
                for year in year_range
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
        print(f"Operation took {end - start} seconds")

    def to_csv(self, file_name) -> None:
        self.df.to_csv(Paths.RAW_DATA_CSV / file_name, index=False)

    def to_parquet(self, file_name) -> None:
        self.df.to_parquet(Paths.RAW_DATA_CSV / file_name, index=False)
