import pandas as pd

from utils.constants import Paths

census_demographics_df = pd.read_csv(Paths.RAW_DATA_CSV / "census_demographic_data.csv")
census_education_df = pd.read_csv(Paths.RAW_DATA_CSV / "census_education_data.csv")
census_income_df = pd.read_csv(Paths.RAW_DATA_CSV / "census_income_data.csv")

census_geography_df = pd.read_csv(Paths.RAW_DATA_CSV / "census_tracts.csv")

demographic_column_mapping = {
    "GeoID": "geo_id",
    "Pop1" : "population",
    "BCT2020": "bct_num",
    # age
    "MdAge": "median_age",
    # race
    "Hsp1P": "hispanic_pct",
    "WNHP": "white_nh_pct",
    "BNHP": "black_nh_pct",
    "ANHP": "asian_nh_pct",
    "ONHP": "other_nh_pct",
    "TwoPlNHP": "two_plus_nh_pct",
    # housing
    "AvgHHSz": "average_hh_size",
}

education_column_mapping = {
    "GEOID": "geo_id",
    # Percent of Population 25 Years and Over whose Highest Education Completed is Less Than High School
    "B15002_calc_pctLTHSE": "less_than_hs_pct",
    # Percent of Population 25 Years and Over whose Highest Education Completed is High School (includes equivalency)
    "B15002_calc_pctHSE": "hs_pct",
    # Percent of Population 25 Years and Over whose Highest Education Completed is Some College
    "B15002_calc_pctSomeCollE": "some_college_pct",
    # Percent of Population 25 Years and Over whose Highest Education Completed is Associate's Degree
    "B15002_calc_pctAAE": "associate_degree_pct",
    # Percent of Population 25 Years and Over whose Highest Education Completed is Bachelor's Degree or Higher
    "B15002_calc_pctGEBAE": "bachelors_or_higher_pct",
}

income_column_mapping = {
    "GEOID": "geo_id",
    # Median Household Income in past 12 months
    "B19049_001E": "median_household_income",
    # Median Household Income in past 12 months, Black or African American Alone Householder
    "B19013B_001E": "median_income_black",
    # Median Household Income in past 12 months, Native American or Alaska Native Alone Householder
    "B19013C_001E": "median_income_native",
    # Median Household Income in past 12 months, Asian Alone Householder
    "B19013D_001E": "median_income_asian",
    # Median Household Income in past 12 months, Hawaiian or Pacific Islander Alone Householder
    "B19013E_001E": "median_income_pacific_islander",
    # Median Household Income in past 12 months, Other Race Householder
    "B19013F_001E": "median_income_other",
    # Median Household Income in past 12 months, Two or More Races Alone Householder
    "B19013G_001E": "median_income_two_plus",
    # Median Household Income in past 12 months, White Alone Householder
    "B19013H_001E": "median_income_white",
    # Median Household Income in past 12 months, Hispanic Alone Householder
    "B19013I_001E": "median_income_hispanic",
}

geography_column_mapping = {
    "GEOID": "geo_id",
    "the_geom": "geometry",
    "NTAName": "neighborhood",
    "BoroName": "borough",
}

census_demographics_df = census_demographics_df[
    demographic_column_mapping.keys()
].rename(columns=demographic_column_mapping)
census_education_df = census_education_df[education_column_mapping.keys()].rename(
    columns=education_column_mapping
)
census_income_df = census_income_df[income_column_mapping.keys()].rename(
    columns=income_column_mapping
)

census_geography_df = census_geography_df[geography_column_mapping.keys()].rename(
    columns=geography_column_mapping
)

census_df = (
    census_demographics_df.merge(census_education_df, on="geo_id")
    .merge(census_income_df, on="geo_id")
    .merge(census_geography_df, on="geo_id")
)

census_df.to_parquet(Paths.PROCESSED_DATA_PARQUET / "census_data.parquet", index=False)
