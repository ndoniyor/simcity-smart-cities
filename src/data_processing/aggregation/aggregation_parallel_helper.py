from concurrent.futures import ProcessPoolExecutor
from utils.constants import Paths

import pandas as pd
from pandas import Timedelta

from time import perf_counter

# can definitely be optimized, could use binary search to limit indexes
def process_census_tract(census_tract, valid_complaints, duplicate_complaints):
    valid_group = valid_complaints[valid_complaints["census_tract"] == census_tract]
    duplicate_group = duplicate_complaints[duplicate_complaints["census_tract"] == census_tract]
    
    valid_group = valid_group.reset_index(drop=True)
    duplicate_group = duplicate_group.reset_index(drop=True)
    
    for i in range(len(valid_group)):
        count = 0
        start_date = valid_group.at[i, "received_date"]
        end_date = valid_group.at[i, "date_closed"] + Timedelta(1, unit="D")
        location_id = valid_group.at[i, "location_id"]

        for j in range(len(duplicate_group)):
            if (
                not duplicate_group.at[j, "seen"]
                and duplicate_group.at[j, "location_id"] == location_id
                and duplicate_group.at[j, "received_date"] <= end_date
                and duplicate_group.at[j, "received_date"] >= start_date
            ):
                count += 1
                duplicate_group.at[j, "seen"] = True
            else:
                break
        valid_group.at[i, "num_requests"] = count
    return valid_group, 1

def process_census_tract_unpack(args):
    return process_census_tract(*args)


def main():
    valid_complaints = pd.read_parquet(Paths.PROCESSED_DATA_PARQUET / "valid_housing_code_post_process.parquet")
    duplicate_complaints = pd.read_parquet(Paths.PROCESSED_DATA_PARQUET / "duplicate_housing_code_post_process.parquet")
    
    duplicate_complaints['seen'] = False

    res_df = pd.DataFrame()
    
    tracts = valid_complaints['census_tract'].unique()
    
    args = [(census_tract, valid_complaints, duplicate_complaints) for census_tract in tracts]
    
    start = perf_counter()
    with ProcessPoolExecutor() as executor:
        list_df = []
        progress = 0
        total = len(valid_complaints['census_tract'].unique())
        for result, increment in executor.map(process_census_tract_unpack, args):
            list_df.append(result)
            progress += increment
            
            elapsed_time = perf_counter() - start
            minutes, seconds = divmod(elapsed_time, 60)
            
            print("\r", end=f"{progress}/{total} Time elapsed: {int(minutes)} min {seconds:.2f} sec")
    
    res_df = pd.concat(list_df)
    res_df.to_parquet(Paths.PROCESSED_DATA_PARQUET / "temp.parquet")


if __name__ == "__main__":
    main()