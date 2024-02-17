from pathlib import Path


class Paths:
    ROOT_PATH = Path(__file__).resolve().parent.parent.parent
    SRC_PATH = ROOT_PATH / "src"
    DATA_PATH = ROOT_PATH / "data"

    PROCESSED_DATA_BASE = DATA_PATH / "processed"
    PROCESSED_DATA_CSV = PROCESSED_DATA_BASE / "csv"
    PROCESSED_DATA_XLSX = PROCESSED_DATA_BASE / "xlsx"
    PROCESSED_DATA_PARQUET = PROCESSED_DATA_BASE / "parquet"

    RAW_DATA_BASE = DATA_PATH / "raw"
    RAW_DATA_CSV = RAW_DATA_BASE / "csv"
    RAW_DATA_XLSX = RAW_DATA_BASE / "xlsx"
    RAW_DATA_PARQUET = RAW_DATA_BASE / "parquet"
    RAW_DATA_JSON = RAW_DATA_BASE / "json"


class Urls:
    OPEN_DATA_URL = "data.cityofnewyork.us"
    ENDPOINT_311 = "erm2-nwe9"
    ENDPOINT_HOUSING_CODE = "wvxf-dwi5"
    ENDPOINT_PARKING = "nc67-uf89"
    ENDPOINT_VACANT_LOT = "r4c5-ndkx"
