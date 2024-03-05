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

#### New York

- [General 311 requests (2010 - Present)](https://data.cityofnewyork.us/Social-Services/311-Service-Requests-from-2010-to-Present/erm2-nwe9)
- [Housing maintenance code complaints (reported)](https://data.cityofnewyork.us/Housing-Development/Housing-Maintenance-Code-Complaints/uwyv-629c)

#### Chicago

- [311 service requests](https://data.cityofchicago.org/Service-Requests/311-Service-Requests/v6vf-nfxy/about_data)

#### San Franciso 
- [311 service requests] (https://data.sfgov.org/widgets/vw6y-z8j6?mobile_redirect=true)

### Validation (Gov't data)

#### New York

- [Pothole work orders](https://data.cityofnewyork.us/Transportation/Street-Pothole-Work-Orders-Closed-Dataset-/x9wy-ing4)
- [Housing maintenance code violations (actual)](https://data.cityofnewyork.us/Housing-Development/Housing-Maintenance-Code-Violations/wvxf-dwi5)

#### Chicago

- [Potholes Patched](https://data.cityofchicago.org/Transportation/Potholes-Patched/wqdh-9gek/about_data)
- [Vacant and Abandoned Buildings - Violations](https://data.cityofchicago.org/Buildings/Vacant-and-Abandoned-Buildings-Violations/kc9i-wq85/about_data)

#### San Franciso 
- [Housing maintenance code violations] (https://data.sfgov.org/Housing-and-Buildings/Notices-of-Violation-issued-by-the-Department-of-B/nbtm-fbw5/about_data)

## To-Do

- [ ] Add census data to NYC data
  - [ ] [Census data](https://www.nyc.gov/site/planning/planning-level/nyc-population/2020-census.page)
  - [ ] Census data organized by census tracts, the following additions need to made to make joining easy:
    - [x] Add census tract to pothole dataset
    - [x] Add census tract to housing code dataset
- [x] Look for other datasets from other cities
- [ ] Add census data to Chicago data
  - [ ] Cross-reference coordinates of 311/gov data to assign census tract numbers from census shapefile
  - [ ] Use census API to batch assign census data
- [x] Write a problem statement; clearly specify what the data will address
- [ ] Causality Analysis
  - [ ] What causes under/overreporting?

