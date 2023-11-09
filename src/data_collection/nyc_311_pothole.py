import pandas as pd
import sys

sys.path.append("..")

from utils.data_collector import DataCollector
from utils.helpers import create_yearly_query, compute_filesize

ENDPOINT = "erm2-nwe9"


def main():
    yearly_queries = []
    dfs = []

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

    collector_311 = DataCollector(endpoint=ENDPOINT)

    for year in range(2010, 2023):
        yearly_queries.append(
            [
                "descriptor='Pothole'",
                "resolution_description='The Department of Transportation inspected this complaint and repaired the problem.'",
                *create_yearly_query(year, 'created_date'),
            ]
        )

    for query in yearly_queries:
        collector_311.collect_data(queries=query, select=columns)
        dfs.append(collector_311.df)

    df = pd.concat(dfs, ignore_index=True)
    print(f"File size: {compute_filesize(df)} MB")

    df.to_csv("../../data/raw/nyc_311_pothole.csv")


if __name__ == "__main__":
    main()
