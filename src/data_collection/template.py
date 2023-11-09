import pandas as pd
import sys

sys.path.append("..")

from utils.data_collector import DataCollector
import utils.helpers as helpers

ENDPOINT = ""


def main():
    yearly_queries = []
    dfs = []

    columns = []

    collector_ = DataCollector(ENDPOINT)

    for year in range(2010, 2023):
        yearly_queries.append([*helpers.create_yearly_query(year)])

    for query in yearly_queries:
        collector_.collect_data(queries=query, select=columns)
        dfs.append(collector_.df)

    df = pd.concat(dfs, ignore_index=True)
    print(f"File size: {helpers.compute_filesize(df)} MB")

    df.to_csv("../../data/raw/.csv")


if __name__ == "__main__":
    main()
