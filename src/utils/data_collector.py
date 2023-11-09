from os import getenv
from pandas import DataFrame, concat, read_csv
from dotenv import load_dotenv
from sodapy import Socrata

DOMAIN = "data.cityofnewyork.us"
CSV_FILE_PATH = "../../data/raw/"

load_dotenv(dotenv_path="../../.env")
app_token = getenv("SOCRATA_TOKEN")


class DataCollector:
    def __init__(self, endpoint=""):
        self.endpoint = endpoint
        self.df = DataFrame()

    def collect_data(self, queries=[], select=[]) -> None:
        dfs = []
        limit = 5000
        offset = 0

        client = Socrata(domain=DOMAIN, app_token=app_token, timeout=10)

        query = " AND ".join(queries) if queries else None

        select_str = ", ".join(select) if select else "*"

        try:
            while True:
                print(f"{offset} records")
                page_results = client.get(
                    self.endpoint,
                    where=query if query else None,
                    select=select_str if select else None,
                    limit=limit,
                    offset=offset,
                )

                if not page_results:
                    break

                dfs.append(DataFrame(page_results))
                offset += limit
            self.df = concat(dfs, ignore_index=True)
        except ValueError as error:
            print("Could not find any files")

    def read_data(self, name) -> None:
        file_path = CSV_FILE_PATH + name + ".csv"
        self.df = read_csv(file_path)

    def to_csv(self, file_name) -> None:
        self.df.to_csv(CSV_FILE_PATH + file_name, index=False)
