"""Pytest configuration file"""
from typing import List
import pandas as pd
import pytest

from . import FIXTURES_DIR, OUTPUT_DIR

@pytest.fixture(scope="session")
def pt_life_expectancy_expected() -> pd.DataFrame:
    """Fixture to load the expected output of the cleaning script"""
    return pd.read_csv(FIXTURES_DIR / "pt_life_expectancy_expected.csv")

@pytest.fixture(scope="session")
def eu_life_expectancy_raw() -> pd.DataFrame:
    """Loads the EU life expectancy raw TSV"""
    return pd.read_csv(FIXTURES_DIR / "eu_life_expectancy_raw.tsv", sep='\t')

@pytest.fixture(scope="function")
def all_regions() -> List[str]:
    """Returns a list with all possible countries"""
    return [
        "AL", "AM", "AT", "AZ", "BE", "BG", "BY", "CH", "CY", "CZ", "DE",
        "DK", "EE", "EL", "ES", "FI", "FR", "GE", "HR", "HU", "IE", "IS",
        "IT", "LI", "LT", "LU", "LV", "ME", "MK", "MT", "NL", "NO", "PL",
        "PT", "RO", "RS", "SE", "SI", "SK", "TR", "UA"
    ]