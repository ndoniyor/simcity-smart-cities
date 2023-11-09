import pandas as pd
import sys

sys.path.append("..")

from utils.data_collector import DataCollector
from utils.helpers import create_yearly_query, compute_filesize

ENDPOINT = "x9wy-ing4"


def main():
    yearly_queries = []
    dfs = []

    columns = [
        "the_geom",
        "RptDate",
        "RptClosed",
    ]

    collector_pothole = DataCollector(ENDPOINT)

    for year in range(2010, 2023):
        yearly_queries.append([*create_yearly_query(year)])

    for query in yearly_queries:
        collector_pothole.collect_data(queries=query, select=columns)
        dfs.append(collector_pothole.df)

    df = pd.concat(dfs, ignore_index=True)
    print(f"File size: {compute_filesize(df)} MB")

    df.to_csv("../../data/raw/nyc_gov_pothole.csv")


if __name__ == "__main__":
    main()
