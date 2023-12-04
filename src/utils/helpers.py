from pyspark.sql import SparkSession
import pandas as pd
from datetime import datetime

from utils.constants import Paths


def create_yearly_query(year, year_field):
    start_of_year = f"{year}-01-01T00:00:00"
    end_of_year = f"{year+1}-01-01T00:00:00"
    query = [f"{year_field} >= '{start_of_year}'", f"{year_field} < '{end_of_year}'"]
    return query


def create_monthly_query(year_month, date_col):
    start_of_month = f"{year_month}-01T00:00:00"
    end_of_month = (
        datetime.strptime(start_of_month, "%Y-%m-%dT%H:%M:%S") + pd.offsets.MonthEnd()
    ).strftime("%Y-%m-%dT%H:%M:%S")
    query = [f"{date_col} >= '{start_of_month}'", f"{date_col} < '{end_of_month}'"]
    return query


def filter_parquet(
    file_name: str, columns: list[str] = [], filters: list[str] = []
) -> pd.DataFrame:
    spark = SparkSession.builder.appName("Parquet Worker").getOrCreate()
    df = spark.read.parquet(str(Paths.RAW_DATA_PARQUET / f"{file_name}.parquet"))
    for condition in filters:
        df = df.filter(condition)
    if columns:
        df = df.select(*columns)
    df = df.toPandas()
    spark.stop()
    return df


def compute_filesize(df):
    return (df.memory_usage(deep=True).sum()) / (1024**2)
