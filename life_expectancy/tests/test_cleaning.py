"""Tests for the cleaning module"""
from pathlib import Path
import pandas as pd

from life_expectancy.cleaning import main
from . import OUTPUT_DIR

CURRENT_DIR = str(Path(__file__).parent)
PATH_RAW_DATASET = f"{CURRENT_DIR}/data/eu_life_expectancy_raw.tsv"

def test_clean_data(pt_life_expectancy_expected):
    """Run the `clean_data` function and compare the output to the expected output"""
    main("PT")
    pt_life_expectancy_actual = pd.read_csv(
        OUTPUT_DIR / "pt_life_expectancy.csv"
    )
    pd.testing.assert_frame_equal(
        pt_life_expectancy_actual, pt_life_expectancy_expected
    )
