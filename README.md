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
- https://data.sfgov.org/City-Infrastructure/311-Cases/vw6y-z8j6/explore/query/SELECT%0A%20%20%60service_request_id%60%2C%0A%20%20%60requested_datetime%60%2C%0A%20%20%60closed_date%60%2C%0A%20%20%60updated_datetime%60%2C%0A%20%20%60status_description%60%2C%0A%20%20%60status_notes%60%2C%0A%20%20%60agency_responsible%60%2C%0A%20%20%60service_name%60%2C%0A%20%20%60service_subtype%60%2C%0A%20%20%60service_details%60%2C%0A%20%20%60address%60%2C%0A%20%20%60street%60%2C%0A%20%20%60supervisor_district%60%2C%0A%20%20%60neighborhoods_sffind_boundaries%60%2C%0A%20%20%60police_district%60%2C%0A%20%20%60lat%60%2C%0A%20%20%60long%60%2C%0A%20%20%60point%60%2C%0A%20%20%60point_geom%60%2C%0A%20%20%60source%60%2C%0A%20%20%60media_url%60%2C%0A%20%20%60bos_2012%60%2C%0A%20%20%60data_as_of%60%2C%0A%20%20%60data_loaded_at%60%2C%0A%20%20%60%3A%40computed_region_6qbp_sg9q%60%2C%0A%20%20%60%3A%40computed_region_qgnn_b9vv%60%2C%0A%20%20%60%3A%40computed_region_26cr_cadq%60%2C%0A%20%20%60%3A%40computed_region_ajp5_b2md%60%2C%0A%20%20%60%3A%40computed_region_rxqg_mtj9%60%2C%0A%20%20%60%3A%40computed_region_yftq_j783%60%2C%0A%20%20%60%3A%40computed_region_jx4q_fizf%60%2C%0A%20%20%60%3A%40computed_region_bh8s_q3mv%60%2C%0A%20%20%60%3A%40computed_region_p5aj_wyqh%60%2C%0A%20%20%60%3A%40computed_region_fyvs_ahh9%60%2C%0A%20%20%60%3A%40computed_region_f58d_8dbm%60%2C%0A%20%20%60%3A%40computed_region_9dfj_4gjx%60%2C%0A%20%20%60%3A%40computed_region_vtsz_7cme%60%2C%0A%20%20%60%3A%40computed_region_n4xg_c4py%60%2C%0A%20%20%60%3A%40computed_region_sruu_94in%60%2C%0A%20%20%60%3A%40computed_region_4isq_27mq%60%2C%0A%20%20%60%3A%40computed_region_viu7_rrfi%60%2C%0A%20%20%60%3A%40computed_region_fcz8_est8%60%2C%0A%20%20%60%3A%40computed_region_pigm_ib2e%60%2C%0A%20%20%60%3A%40computed_region_9jxd_iqea%60%2C%0A%20%20%60%3A%40computed_region_6ezc_tdp2%60%2C%0A%20%20%60%3A%40computed_region_6pnf_4xz7%60%2C%0A%20%20%60%3A%40computed_region_h4ep_8xdi%60%2C%0A%20%20%60%3A%40computed_region_nqbw_i6c3%60%2C%0A%20%20%60%3A%40computed_region_2dwj_jsy4%60%2C%0A%20%20%60%3A%40computed_region_y6ts_4iup%60%2C%0A%20%20%60%3A%40computed_region_jwn9_ihcz%60/page/filter (alt link)

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

