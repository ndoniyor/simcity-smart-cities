import pandas as pd
import sys

sys.path.append("..")

from utils.data_collector import DataCollector

ENDPOINT = "x9wy-ing4"


def main():
    year_range = range(2010, 2024)

    columns = [
        "DefNum",
        "the_geom",
        "RptDate",
        "RptClosed",
        "OnPrimName"
    ]

    collector_311 = DataCollector(
        endpoint=ENDPOINT,
        filters=[],
        columns=columns,
        date_col="RptDate",
    )
    collector_311.collect_data(years=year_range)
    collector_311.to_csv("nyc_gov_pothole.csv")


if __name__ == "__main__":
    main()
