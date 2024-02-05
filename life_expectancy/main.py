""" Main script to load, clean and save the data"""
#--------------------------------------------------------------------
# IMPORTS
#--------------------------------------------------------------------
import argparse
from pathlib import Path
import pandas as pd
from life_expectancy.utils.cleaning import TSVCleaner, JSONCleaner
from life_expectancy.utils.load_save_data import TSVLoader, JSONLoader, save_data
from life_expectancy.utils.regions import Region

#--------------------------------------------------------------------
# VARIABLE DECLARATION
#--------------------------------------------------------------------

CURRENT_DIR = str(Path(__file__).parent)
PATH_RAW_DATASET = f"{CURRENT_DIR}/data/eu_life_expectancy_raw.tsv"
PATH_CLEAN_DATASET = f"{CURRENT_DIR}/data/"

#--------------------------------------------------------------------
# MAIN
#--------------------------------------------------------------------

def main(file_path: Path, region: Region = Region.PT) -> pd.DataFrame:
    """main function"""

    file_type = file_path.suffix
    
    if file_type == '.tsv':
        data_loader = TSVLoader()
        data_cleaner = TSVCleaner(region)
    elif file_type == '.json':
        data_loader = JSONLoader()
        data_cleaner = JSONCleaner(region)

    data = data_loader.load_data(file_path)
    cleaned_data = data_cleaner.clean_data(data)
    save_data(cleaned_data, region)

    return cleaned_data

if __name__ == "__main__":  
    parser = argparse.ArgumentParser()
    parser.add_argument('file_path')
    parser.add_argument('region')
    args = parser.parse_args()
    main(args.file_path, args.region)