# ESE 440 Senior Design Project - Smart Cities

This project focuses on analyzing data from the city of New York to derive insights on various city services, using datasets fetched via the sodapy API. Analyses are performed using Python libraries such as `pandas`, `geopandas`, `numpy`, and `matplotlib`.

## Getting Started

- Clone repository
- Make sure you're in the repository base directory
- Create Python Virtual Environment

```
python3 -m venv simcity_env
```

- Now activate the environment with

```
source ./simcity_env/bin/activate
```

- Now install dependencies with:

```
pip install -r requirements.txt
```

## Gathering data

Scripts to pull data are located in `src/data_collection/`:

- `cd` into `./src/data_collection/`
- Run the following:

```
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
- [Parking violations](https://data.cityofnewyork.us/City-Government/Open-Parking-and-Camera-Violations/nc67-uf89)
- [Plowing data](https://data.cityofnewyork.us/view/34hf-h2fw)
- [Housing maintenance code violations (actual)](https://data.cityofnewyork.us/Housing-Development/Housing-Maintenance-Code-Violations/wvxf-dwi5)

## Data alignment

The data here needs to be aligned, so that we can validate user requests against the government provided data
Currently aligned data:
| Base set | Validation set | Alignment File|
|--|--|--|
|General 311 requests (pothole requests only) | Pothole work orders | `src/data_processing/align_pothole.ipynb`|
|Housing code complaints | Housing code violations | `src/data_processing/align_housing_code.ipynb`|

## To-Do

- [ ] Experiment with Left/Right/Inner/Outer Joins to find out more about the data
  - [ ] Organize by:
    - Left with no right (No government action to citizen report)
    - Right with no left (Government action without citizen report)
    - Both (User report and government action)
- [ ] Fix alignment of housing code to include open violations - **IN PROGRESS**
- [ ] Align all data
- [ ] Causality Analysis
  - [ ] What causes under/overreporting?
- [ ] Describe regions by socioeconomic status
  - [ ] Use Census data
