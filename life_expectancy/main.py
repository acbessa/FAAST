""" Main script to load, clean and save the data"""
#--------------------------------------------------------------------
# IMPORTS
#--------------------------------------------------------------------
import argparse
from pathlib import Path
import os
import pandas as pd
from life_expectancy.utils.cleaning import TSVCleaner, ZIPCleaner
from life_expectancy.utils.load_save_data import TSVLoader, ZIPLoader, save_data
from life_expectancy.utils.regions import Region

#--------------------------------------------------------------------
# VARIABLE DECLARATION
#--------------------------------------------------------------------

CURRENT_DIR = str(Path(__file__).parent)
PATH_CLEAN_DATASET = f"{CURRENT_DIR}/data/"

#--------------------------------------------------------------------
# MAIN
#--------------------------------------------------------------------

def main(file_path: Path, region: Region = Region.PT) -> pd.DataFrame:
    """main function"""

    _, extension = os.path.splitext(file_path)

    file_type = extension

    print(file_type)

    if file_type == '.tsv':
        data_loader = TSVLoader()
        data_cleaner = TSVCleaner(region)
    elif file_type == '.zip':
        data_loader = ZIPLoader()
        data_cleaner = ZIPCleaner(region)

    data = data_loader.load_data(file_path)
    cleaned_data = data_cleaner.clean_data(data)
    save_data(cleaned_data, region, PATH_CLEAN_DATASET)

    return cleaned_data

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('file_path')
    parser.add_argument('region')
    args = parser.parse_args()
    main(args.file_path, args.region)
