import pandas as pd
import sys

sys.path.append("..")

from utils.data_collector import DataCollector
from utils.helpers import create_yearly_query, compute_filesize

ENDPOINT = "x9wy-ing4"


def main():
    year_range = range(2010,2023)

    columns = [
        "the_geom",
        "RptDate",
        "RptClosed",
    ]

    collector_311 = DataCollector(
        endpoint=ENDPOINT,
        filters=[],
        columns=columns,
        date_col="created_date",
    )
    collector_311.collect_data(years=year_range)
    collector_311.to_csv("nyc_gov_pothole.csv")


if __name__ == "__main__":
    main()
