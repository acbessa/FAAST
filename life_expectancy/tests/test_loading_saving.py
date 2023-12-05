"""Test for load_data function"""
from unittest.mock import patch
import pandas as pd
from life_expectancy.cleaning import load_data, save_dataframe_csv
from . import FIXTURES_DIR

def test_load_data():
    """Test the data loading"""
    
    loaded_df = load_data(FIXTURES_DIR / "eu_life_expectancy_raw.tsv")
    
    assert loaded_df.shape == (14448, 63)


@patch("pandas.DataFrame.to_csv")
def test_save_data(patched_to_csv):
    """Test the data saving"""
    
    df_to_save = pd.read_csv(FIXTURES_DIR / "pt_life_expectancy_expected.csv")
    output_path = "dummy_path"
    expected_output_path = output_path + "_life_expectancy.csv"
    save_dataframe_csv(df_to_save, output_path, "")
    patched_to_csv.assert_called_once_with(expected_output_path, index=False)
    
    