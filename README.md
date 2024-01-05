# ESE 440 Senior Design Project - Smart Cities

This project focuses on analyzing data from the city of New York to derive insights on various city services, using datasets fetched via the sodapy API. Analyses are performed using Python libraries such as `pandas`, `geopandas`, `numpy`, and `matplotlib`.

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

## Gathering data

Scripts to pull data are located in `src/data_collection/`:

- `cd` into `./src/data_collection/`
- Run the following:

```shell
python <name_of_script>.py
```

- This will pull the data and put it into a csv file in `data/raw/`

## Datasets

### Base (User data)

- [General 311 requests (2010 - Present)](https://data.cityofnewyork.us/Social-Services/311-Service-Requests-from-2010-to-Present/erm2-nwe9)
- [Housing maintenance code complaints (reported)](https://data.cityofnewyork.us/Housing-Development/Housing-Maintenance-Code-Complaints/uwyv-629c)

### Validation (Gov't data)

- [Pothole work orders](https://data.cityofnewyork.us/Transportation/Street-Pothole-Work-Orders-Closed-Dataset-/x9wy-ing4)
- [Vacant lot cleaning](https://data.cityofnewyork.us/City-Government/Lot-Cleaning-Dispositions-No-Longer-Maintained-/r4c5-ndkx)
- [Housing maintenance code violations (actual)](https://data.cityofnewyork.us/Housing-Development/Housing-Maintenance-Code-Violations/wvxf-dwi5)

## Data alignment

The data here needs to be aligned, so that we can validate user requests against the government provided data
Currently aligned data:
| Base set | Validation set | Alignment File |
|----------|----------------|----------------|
|General 311 requests (pothole requests only) | Pothole work orders | `src/data_processing/align_pothole.ipynb`|
|Housing code complaints | Housing code violations | `src/data_processing/align_housing_code.ipynb`|

## To-Do

- [ ] Join aggregated data with census data
  - [ ] [Census data](https://www.nyc.gov/site/planning/planning-level/nyc-population/2020-census.page)
  - [ ] Census data organized by census tracts, the following additions need to made to make joining easy:
    - [ ] Add census tract to pothole dataset
    - [ ] Add census tract to housing code dataset
    - [ ] Add census tract to parking dataset
    - [ ] Add census tract to vacant lot dataset
- [ ] Write a problem statement; clearly specify what the data will address
- [ ] Find another set for parking issues
  - [Collection of issued tickets](https://data.cityofnewyork.us/browse?Data-Collection_Data-Collection=DOF+Parking+Violations+Issued&q=&sortBy=alpha&utf8=%E2%9C%93)
- [ ] Causality Analysis
  - [ ] What causes under/overreporting?
