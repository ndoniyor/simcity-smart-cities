import pandas as pd
import sys

sys.path.append("..")

from utils.data_collector import DataCollector
import utils.helpers as helpers

ENDPOINT = "uwyv-629c"


def main():
    yearly_queries = []
    dfs = []

    columns = [
        "complaintid",
        "buildingid",
        "borough",
        "apartment",
        "status",
        "statusdate"
    ]

    collector_housing = DataCollector(ENDPOINT)

    for year in range(2010, 2023):
        yearly_queries.append(
            ["status='CLOSE'", *helpers.create_yearly_query(year, "statusdate")]
        )

    for query in yearly_queries:
        collector_housing.collect_data(queries=query, select=columns)
        dfs.append(collector_housing.df)

    df = pd.concat(dfs, ignore_index=True)
    print(f"File size: {helpers.compute_filesize(df)} MB")

    df.to_csv("../../data/raw/nyc_user_housing_violation.csv")


if __name__ == "__main__":
    main()
