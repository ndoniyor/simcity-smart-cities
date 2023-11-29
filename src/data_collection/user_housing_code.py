import pandas as pd
import sys

sys.path.append("..")
from utils.data_collector import DataCollector

ENDPOINT = "uwyv-629c"


def main():
    year_range = range(2010, 2023)
    columns = [
        "complaintid",
        "buildingid",
        "borough",
        "apartment",
        "status",
        "statusdate",
    ]

    collector_housing = DataCollector(
        endpoint=ENDPOINT,
        #filters=["status='CLOSE'"],
        filters=[],
        columns=columns,
        date_col="statusdate",
    )
    collector_housing.collect_data(years=year_range)
    collector_housing.df.to_csv("../../data/raw/nyc_user_housing_violation_no_filter.csv")


if __name__ == "__main__":
    main()
