import pandas as pd
import sys

sys.path.append("..")

from utils.data_collector import DataCollector
import utils.helpers as helpers

ENDPOINT = "wvxf-dwi5"


def main():
    yearly_queries = []
    dfs = []

    columns = [
        "violationid",
        "buildingid",
        "apartment",
        "inspectiondate",
        "approveddate",
        "violationstatus",
        "currentstatus",
    ]

    collector_housing = DataCollector(ENDPOINT)

    for year in range(2010, 2023):
        yearly_queries.append(
            ["currentstatus='VIOLATION CLOSED'", *helpers.create_yearly_query(year, "currentstatusdate")]
        )

    for query in yearly_queries:
        collector_housing.collect_data(queries=query, select=columns)
        dfs.append(collector_housing.df)

    df = pd.concat(dfs, ignore_index=True)
    print(f"File size: {helpers.compute_filesize(df)} MB")

    df.to_csv("../../data/raw/nyc_gov_housing_violation.csv")


if __name__ == "__main__":
    main()
