""" Load and save data script """
#--------------------------------------------------------------------
# IMPORTS
#--------------------------------------------------------------------
from abc import ABC, abstractmethod
import pandas as pd
from zipfile import ZipFile
import json

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

class ZIPLoader(DataLoaderStrategy):
    """class for  ZIP data"""
    
    #def load_data(self, file_path) -> pd.DataFrame:
        #'''
        #Loads the json file that contains the data
        #returns:
        #    data(Pandas DataFrame): Loaded dataframe
        #'''

        # load input json dataframe
    #    return pd.read_json(file_path)
    
    def load_data(self, file_path) -> pd.DataFrame:
        '''
        Loads the json file that contains the data
        returns:
            data(Pandas DataFrame): Loaded dataframe
        '''
        
        with ZipFile(file_path, "r") as zip_file:
            with zip_file.open(zip_file.namelist()[0]) as json_file:
                return pd.DataFrame(json.loads(json_file.read()))
    
#--------------------------------------------------------------------
# SAVE DATA
#--------------------------------------------------------------------

def save_data(dataframe: pd.DataFrame, region, path) -> None:
    '''
    Saves the input dataframe into a csv file
    Args:
        data (Pandas DataFrame): DataFrame to be saved
    '''

    path = path + region + "_life_expectancy.csv"
    dataframe.to_csv(path, index = False)
