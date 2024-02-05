""" Cleaning data script """
#--------------------------------------------------------------------
# IMPORTS
#--------------------------------------------------------------------
from abc import ABC, abstractmethod
import pandas as pd
from life_expectancy.utils.regions import Region

#--------------------------------------------------------------------
# VARIABLE DECLARATION
#--------------------------------------------------------------------

NEW_COL_NAMES = ['unit', 'sex', 'age', 'region']

#--------------------------------------------------------------------
# ABSTRACT CLASS
#--------------------------------------------------------------------

class DataCleanerStrategy(ABC):
    """Abstract class for cleaning data"""

    @abstractmethod
    def clean_data(self, data: pd.DataFrame, region: Region) -> pd.DataFrame:
        """Abstract method to clean the data"""

#--------------------------------------------------------------------
# CLASS FOR TSV
#--------------------------------------------------------------------

class TSVCleaner(DataCleanerStrategy):
    """Class for cleaning TSV data"""

    def __init__(self, region: Region):
        
        self.region = region
        
    def split_first_four_columns(self, dataset):
        """ Slipts the frist column of the dataset into four different columns """
        old_col = 'unit,sex,age,geo\\time'

        dataset[NEW_COL_NAMES] = dataset[old_col].str.split(',', expand=True)
        dataset = dataset.drop(columns=[old_col])

        return dataset

    def get_date_columns(self, dataset):
        """ Gets all the columns that represent a date """
        date_columns = dataset.drop(columns = NEW_COL_NAMES).columns

        return date_columns

    def unpivot_date_columns(self, dataset):
        """ Unpivots the date columns, turning them into data """
        date_columns = self.get_date_columns(dataset)

        return pd.melt(dataset, value_vars = date_columns,\
                                        id_vars = NEW_COL_NAMES,\
                                        var_name = 'year',\
                                        value_name='value')

    def ensure_year_as_int(self, dataset):
        """ Makes sure the dates are intergers """
        dataset['year'] = dataset['year'].astype(int)

        return dataset

    def ensure_value_as_float(self, dataset):
        """ Makes sure the values are floats and removes NaNs"""
        dataset['value'] = (dataset['value'].str.extract(r'(\d+\.?\d*)').astype(float))
        dataset = dataset.dropna()

        return dataset

    def filter_region(self, dataset, region):
        """ Filters the dataset by region"""

        dataset = dataset[dataset['region'] == region.value]

        return dataset

    def clean_data(self, data):
        """ Cleans and returns the dataset """

        dataset = self.split_first_four_columns(data)
        dataset = self.unpivot_date_columns(dataset)
        dataset = self.ensure_year_as_int(dataset)
        dataset = self.ensure_value_as_float(dataset)
        dataset = self.filter_region(dataset, self.region)

        return dataset

#--------------------------------------------------------------------
# CLASS FOR JSON
#--------------------------------------------------------------------

class JSONCleaner(DataCleanerStrategy):
    """Class for cleaning JSON data"""

    def __init__(self, region: Region):
        
        self.region = region
        
    
    def rename_cols(self, dataset):
        
        dataset = dataset.rename(columns={"country": "region", "life_expectancy": "value"})
        
        return dataset
    
    def drop_columns(self, dataset):

        dataset = dataset.drop(columns=["flag", "flag_detail"], axis = 1)
        
        return dataset

    def filter_region(self, dataset, region):
        
        filtered_df = dataset[dataset["region"] == region.value]

        return filtered_df
    
    def clean_data(self, data):
        """ Cleans and returns the dataset """

        dataset = self.rename_cols(data)
        dataset = self.drop_columns(dataset)
        dataset = self.filter_region(dataset, self.region)

        return dataset
    