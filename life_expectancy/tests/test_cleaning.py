"""Tests for the cleaning module"""
from pathlib import Path
import pandas as pd

from life_expectancy.cleaning import main
from . import FIXTURES_DIR

def test_clean_data(pt_life_expectancy_expected):
    """Run the `clean_data` function and compare the output to the expected output"""
   
    pt_life_expectancy_actual = main(
        "PT",
        FIXTURES_DIR / "eu_life_expectancy_raw.tsv"
    ).reset_index(drop=True)
    
    pt_life_expectancy_expected = pd.read_csv(
        FIXTURES_DIR / "pt_life_expectancy_expected.csv"
    )
    
    pd.testing.assert_frame_equal(
        pt_life_expectancy_actual, pt_life_expectancy_expected
    )
