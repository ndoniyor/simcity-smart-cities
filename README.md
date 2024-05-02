# ESE 440 Senior Design Project - Smart Cities

This project focuses on analyzing data from the city of New York to derive insights on various city services, using datasets fetched via the sodapy API. Analyses are performed using Python libraries such as `pandas`, `geopandas`, `numpy`, and `matplotlib`.

The goal of this is project is to explore differences between what citizens report and what actions the government takes. We want to see if there's a connection between how quickly and how much the government responds, and the demographics of different areas. This will help us better understand how well the government's responses match up with what citizens are reporting. 


## Getting Started

- Clone repository
- Make sure you're in the repository base directory
- Create Python Virtual Environment:

```shell
python3 -m venv simcity_env
```

- Now activate the environment with:

```shell
source ./simcity_env/bin/activate
```

- Now install dependencies with:

```shell
pip install -r requirements.txt
```

## Gathering data [DEPRECATED]

Scripts to pull data are located in `src/data_collection/`:

- `cd` into `./src/data_collection/`
- Run the following:

```shell
python <name_of_script>.py
```

- This will pull the data and put it into a csv file in `data/raw/`


## New Data Gathering
OpenData API had too many issues with large data so we just pulled the data ourselves. Therefore the notebooks assume the data is already downloaded. 

So to start extract the data archive to a `data` folder in the base root of the directory or the `DATA_PATH` shown below.

I used `pathlib` to make directory constants to make things simpler, here's what they mean:

```
ROOT_PATH = Root project directory
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
```

Since the processed data is provided, you can pick up from the `data_analysis` folder

## Datasets

### Schema
The base datasets have data dictionaries that can be found in the portals. But the following is the data dictionary of the pothole data used for the causality analysis

```json
{
  "borough": "Borough of complaint",
  "neighborhood": "Neighborhood of complaint (based on census dataset)",
  "street": "Street of complaint (this is either an intersection of 2 streets, or a main street bounded by 2 other streets)",
  "year_month": "MM/YYYY date of complaint group",
  "report_count": "Number of reports in grouped 'year_month' + 'street' combination",
  "rating": "Ground truth street condition rating (from street pavement ratings dataset)",
  "population_density": "Population density (population / area) of the CENSUS BLOCK",
  "street_length": "Length of street the sidewalk is on",
  "geometry": "Coordinates of pothole group (centroid)",
  "median_age": "Median age of CENSUS BLOCK of CENSUS BLOCK of street",
  "hispanic_pct": "Percentage of hispanic residents of CENSUS BLOCK of street",
  "white_nh_pct": "Percentage of white (non:hispanic) residents of CENSUS BLOCK of street",
  "black_nh_pct": "Percentage of black (non:hispanic) residents of CENSUS BLOCK of street",
  "asian_nh_pct": "Percentage of asian (non:hispanic) residents of CENSUS BLOCK of street",
  "average_hh_size": "Average househild size of CENSUS BLOCK of street",
  "less_than_hs_pct": "Percentage of residents with less than high school degree of CENSUS BLOCK of street",
  "hs_pct": "Percentage of residents with  high school degree of CENSUS BLOCK of street",
  "some_college_pct": "Percentage of residents with some college experience of CENSUS BLOCK of street",
  "associate_degree_pct": "Percentage of residents with associate's degree of CENSUS BLOCK of street",
  "bachelors_or_higher_pct": "Percentage of residents with bachelor's degree of CENSUS BLOCK of street",
  "median_household_income": "Median household income of CENSUS BLOCK of street",
  "reporting_ratio": "Number of reports per group normalized by population_density and street length",
  "normalized_reporting_ratio": "Same as before but mapped to 0: 10 range",
  "reporting_difference": "Difference of 'normalized_reporting_ratio' and 'rating', represnts over/underreporting rate"
}
```

### Base (User data)

#### New York

- [General 311 requests (2010 - Present)](https://data.cityofnewyork.us/Social-Services/311-Service-Requests-from-2010-to-Present/erm2-nwe9)
- [Housing maintenance code complaints (reported)](https://data.cityofnewyork.us/Housing-Development/Housing-Maintenance-Code-Complaints/uwyv-629c)

#### Chicago

- [311 service requests](https://data.cityofchicago.org/Service-Requests/311-Service-Requests/v6vf-nfxy/about_data)

#### San Franciso 
- [311 service requests](https://data.sfgov.org/widgets/vw6y-z8j6?mobile_redirect=true)

### Validation (Gov't data)

#### New York

- [Pothole work orders](https://data.cityofnewyork.us/Transportation/Street-Pothole-Work-Orders-Closed-Dataset-/x9wy-ing4)
- [Housing maintenance code violations (actual)](https://data.cityofnewyork.us/Housing-Development/Housing-Maintenance-Code-Violations/wvxf-dwi5)

#### Chicago

- [Potholes Patched](https://data.cityofchicago.org/Transportation/Potholes-Patched/wqdh-9gek/about_data)
- [Vacant and Abandoned Buildings - Violations](https://data.cityofchicago.org/Buildings/Vacant-and-Abandoned-Buildings-Violations/kc9i-wq85/about_data)

#### San Franciso 
- [Housing maintenance code violations] (https://data.sfgov.org/Housing-and-Buildings/Notices-of-Violation-issued-by-the-Department-of-B/nbtm-fbw5/about_data)
https://data.sfgov.org/Housing-and-Buildings/Department-of-Building-Inspection-Complaints-All-D/gm2e-bten/about_data
