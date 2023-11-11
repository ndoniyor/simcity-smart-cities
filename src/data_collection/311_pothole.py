import pandas as pd
import sys

sys.path.append("..")
from utils.data_collector import DataCollector

ENDPOINT = "erm2-nwe9"


def main():
    year_range = range(2010, 2023)

    columns = [
        "unique_key",
        "created_date",
        "closed_date",
        "incident_zip",
        "incident_address",
        "street_name",
        "cross_street_1",
        "cross_street_2",
        "intersection_street_1",
        "intersection_street_2",
        "address_type",
        "city",
        "resolution_action_updated_date",
        "bbl",
        "borough",
        "x_coordinate_state_plane",
        "y_coordinate_state_plane",
        "park_borough",
        "latitude",
        "longitude",
        "descriptor",
    ]
    filters = [
        "descriptor='Pothole'",
        "resolution_description='The Department of Transportation inspected this complaint and repaired the problem.'",
    ]

    collector_311 = DataCollector(
        endpoint=ENDPOINT,
        filters=filters,
        columns=columns,
        date_col="created_date",
    )
    collector_311.collect_data(years=year_range)
    collector_311.to_csv("nyc_311_pothole.csv")


if __name__ == "__main__":
    main()
