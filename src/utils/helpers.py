import pandas as pd 

def create_yearly_query(year, year_field):
    start_of_year = f"{year}-01-01T00:00:00"
    end_of_year = f"{year+1}-01-01T00:00:00"
    query = [f"{year_field} >= '{start_of_year}'", f"{year_field} < '{end_of_year}'"]
    return query

def compute_filesize(df):
    return (df.memory_usage(deep=True).sum()) / (1024**2)