"""Test for the regions class"""
from life_expectancy.utils.regions import Region

def test_get_countries(all_regions):
    """Test the `get_regions` method"""
    assert Region.get_regions() == all_regions