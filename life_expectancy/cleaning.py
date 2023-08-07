""" The code in this file loads, cleans and saves a dataset """
from pathlib import Path
import argparse
import pandas as pd

#--------------------------------------------------------------------
# VARIABLES
#--------------------------------------------------------------------

CURRENT_DIR = str(Path(__file__).parent)
PATH_RAW_DATASET = f"{CURRENT_DIR}/data/eu_life_expectancy_raw.tsv"
PATH_CLEAN_DATASET = f"{CURRENT_DIR}/data/pt_life_expectancy.csv"
new_col_names = ['unit', 'sex', 'age', 'region']

#--------------------------------------------------------------------
# FUNÇÔES
#--------------------------------------------------------------------

def load_tsv_dataset(path):
    """ Loads the tsv dataset"""
    dataset = pd.read_csv(path, sep='\t')

    return dataset

def split_first_four_columns(dataset):
    """ Slipts the frist column of the dataset into four different columns """
    old_col = 'unit,sex,age,geo\\time'

    dataset[new_col_names] = dataset[old_col].str.split(',', expand=True)
    dataset = dataset.drop(columns=[old_col])

    return dataset

def get_date_columns(dataset):
    """ Gets all the columns that represent a date """
    date_columns = dataset.drop(columns = new_col_names).columns

    return date_columns

def unpivot_date_columns(dataset):
    """ Unpivots the date columns, turning them into data """
    date_columns = get_date_columns(dataset)

    unpivoted_df = pd.melt(dataset, value_vars = date_columns,\
                                    id_vars = new_col_names,\
                                    var_name = 'year',\
                                    value_name='value')

    return unpivoted_df

def ensure_year_as_int(dataset):
    """ Makes sure the dates are intergers """
    dataset['year'] = dataset['year'].astype(int)

    return dataset

def ensure_value_as_float(dataset):
    """ Makes sure the values are floats and removes NaNs"""
    dataset['value'] = (dataset['value'].str.extract(r'(\d+\.?\d*)').astype(float))
    dataset = dataset.dropna()

    return dataset

def filter_region(dataset, region):
    """ Filters the dataset by region, default = PT """
    dataset = dataset[dataset['region'] == region]

    return dataset

def save_dataframe_csv(dataset, path):
    """ Saves the filtered dataset """
    dataset.to_csv(path, index = False)

def clean_data(region = 'PT') -> None:
    """ Loads, cleans ans saves the dataset """

    dataset = load_tsv_dataset(PATH_RAW_DATASET)
    dataset = split_first_four_columns(dataset)
    dataset = unpivot_date_columns(dataset)
    dataset = ensure_year_as_int(dataset)
    dataset = ensure_value_as_float(dataset)
    dataset = filter_region(dataset, region)
    save_dataframe_csv(dataset, PATH_CLEAN_DATASET)

#--------------------------------------------------------------------
# MAIN
#--------------------------------------------------------------------

if __name__ == "__main__":  # pragma: no cover
    parser = argparse.ArgumentParser(description='Clean data and filter by country')
    parser.add_argument('--country', help='Country to use as filter')
    args = parser.parse_args()
    clean_data(args.country)
