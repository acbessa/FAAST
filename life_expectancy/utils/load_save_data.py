""" Load and save data script """
#--------------------------------------------------------------------
# IMPORTS
#--------------------------------------------------------------------
from abc import ABC, abstractmethod
import pandas as pd

#--------------------------------------------------------------------
# ABSTRACT CLASS (LOADING)
#--------------------------------------------------------------------

class DataLoaderStrategy(ABC):
    """Abstract class for loading data"""
    @abstractmethod
    def load_data(self, file_path):
        """Abstract method to load the data"""

#--------------------------------------------------------------------
# CLASS FOR TSV (LOADING)
#--------------------------------------------------------------------

class TSVLoader(DataLoaderStrategy):
    """class for loading TSV data"""

    def load_data(self, file_path) -> pd.DataFrame:
        '''
        Loads the csv file that contains the data
        returns:
            data(Pandas DataFrame): Loaded dataframe
        '''

        # load input tsv dataframe
        return pd.read_csv(file_path, sep='\t')
    
#--------------------------------------------------------------------
# CLASS FOR JSON (LOADING)
#--------------------------------------------------------------------

class JSONLoader(DataLoaderStrategy):
    """class for cleaning JSON data"""

    def load_data(self, file_path) -> pd.DataFrame:
        '''
        Loads the json file that contains the data
        returns:
            data(Pandas DataFrame): Loaded dataframe
        '''

        # load input json dataframe
        return pd.read_json(file_path, compression="infer")
    
#--------------------------------------------------------------------
# SAVE DATA
#--------------------------------------------------------------------

def save_data(dataframe: pd.DataFrame, region) -> None:
    '''
    Saves the input dataframe into a csv file
    Args:
        data (Pandas DataFrame): DataFrame to be saved
    '''

    path = path + region + "_life_expectancy.csv"
    dataframe.to_csv(path, index = False)
