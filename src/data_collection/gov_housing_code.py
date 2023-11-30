import pandas as pd
from concurrent.futures import ThreadPoolExecutor, as_completed
import sys

sys.path.append("..")
from utils.data_collector import DataCollector

ENDPOINT = "wvxf-dwi5"


def main():
    year_range = range(2010, 2024)

    columns = ["inspectiondate", "block"]

    collector_housing = DataCollector(
        endpoint=ENDPOINT,
        filters=[],
        columns=columns,
        date_col="inspectiondate",
    )
    collector_housing.collect_data(years=year_range)

    collector_housing.to_csv("../../data/raw/nyc_gov_housing_violation_no_filter.csv")


if __name__ == "__main__":
    main()
