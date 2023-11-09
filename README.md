# ESE 440 Senior Design Project - Smart Cities

This project focuses on analyzing data from the city of New York to derive insights on various city services, using datasets fetched via the sodapy API. Analyses are performed using Python libraries such as `pandas`, `geopandas`, `numpy`, and `matplotlib`.

## Getting Started
* Clone repository
* Make sure you're in the repository base directory
* Create Python Virtual Environment
```
python3 -m venv simcity_env
```
* Now activate the environment with
```
source ./simcity_env/bin/activate
```
* Now install dependencies with:
```
pip install -r requirements.txt
```

## Gathering data
Scripts to pull data are located in `src/data_collection/`:
* `cd` into `./src/data_collection/`
* Run the following:
```
python <name_of_script>.py
```
* This will pull the data and put it into a csv file in `data/raw/`
