import os
import pandas as pd
from dotenv import load_dotenv
from sodapy import Socrata

DOMAIN = "data.cityofnewyork.us"
ENDPOINT = "jrb2-thup"
CSV_FILE_PATH = '../../data/raw/nyc_data.csv'

load_dotenv(dotenv_path='../../.env')
app_token = os.getenv("SOCRATA_TOKEN") 

client = Socrata(
    domain=DOMAIN,
    app_token=app_token,
    timeout=10
)

dataframes = []

limit = 5000  
offset = 0
while True:
    print(f'{offset} records')
    page_results = client.get(ENDPOINT, limit=limit, offset=offset)
    
    if not page_results:
        break
    
    dataframes.append(pd.DataFrame(page_results))
    offset += limit

df = pd.concat(dataframes,ignore_index=True)

df.to_csv(CSV_FILE_PATH,index=False)
