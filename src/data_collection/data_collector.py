from os import getenv
from pandas import (
    DataFrame,
    concat,
)
from dotenv import load_dotenv
from sodapy import Socrata

DOMAIN = "data.cityofnewyork.us"
CSV_FILE_PATH = "../../data/raw/"

load_dotenv(dotenv_path="../../.env")
app_token = getenv("SOCRATA_TOKEN")


class DataCollector:
    def __init__(self, endpoint: str) -> None:
        self.endpoint = endpoint

        self.client = Socrata(domain=DOMAIN, app_token=app_token, timeout=10)

    def collect_data(self) -> DataFrame:
        dfs = []
        limit = 5000
        offset = 0

        while True:
            print(f"{offset} records")
            page_results = self.client.get(self.endpoint, limit=limit, offset=offset)

            if not page_results:
                break

            dfs.append(DataFrame(page_results))
            offset += limit
        return concat(dfs, ignore_index=True)

    def to_csv(self, df, name) -> None:
        df.to_csv(CSV_FILE_PATH + name, index=False)
