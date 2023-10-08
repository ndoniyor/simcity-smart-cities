# ESE 440 Senior Design Project - Smart Cities

This project focuses on analyzing data from the city of New York to derive insights on various city services, using datasets fetched via the sodapy API. Analyses are performed using Python libraries such as `pandas`, `numpy`, and `matplotlib`.

## Getting Started
* Clone repository
* Make sure you're in the repository base directory
* Make sure Conda is installed
* Create conda environment from environment.yml:
```
conda env create -f environment.yml
```
* Now activate the environment with
```
conda activate simcity
```
If this doesn't work try
```
source activate simcity
```
## Gathering data
Currently only one data script exists so to run that:
* `cd` into `./src/data_collection/`
* Run the following:
```
python nyc_311.py
```
* This will pull the data and put it into a csv file in `./data/raw/nyc_data.csv`
