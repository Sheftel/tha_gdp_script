import pytest

from app.reports import average_gdp

"""
Test Cases

1. Average GDP - returns correct data
"""


def test_average_gdp_success():
    sample_data = [
        {
            "country": "United States",
            "year": "2023",
            "gdp": "25462",
            "gdp_growth": "2.1",
            "inflation": "3.4",
            "unemployment": "3.7",
            "population": "339",
            "continent": "North America",
        },
        {
            "country": "United States",
            "year": "2022",
            "gdp": "23315",
            "gdp_growth": "2.1",
            "inflation": "8.0",
            "unemployment": "3.6",
            "population": "338",
            "continent": "North America",
        },
        {
            "country": "United States",
            "year": "2021",
            "gdp": "22994",
            "gdp_growth": "5.9",
            "inflation": "4.7",
            "unemployment": "5.3",
            "population": "337",
            "continent": "North America",
        },
        {
            "country": "China",
            "year": "2023",
            "gdp": "17963",
            "gdp_growth": "5.2",
            "inflation": "2.5",
            "unemployment": "5.2",
            "population": "1425",
            "continent": "Asia",
        },
        {
            "country": "China",
            "year": "2022",
            "gdp": "17734",
            "gdp_growth": "3.0",
            "inflation": "2.0",
            "unemployment": "5.6",
            "population": "1423",
            "continent": "Asia",
        },
        {
            "country": "China",
            "year": "2021",
            "gdp": "17734",
            "gdp_growth": "8.4",
            "inflation": "1.0",
            "unemployment": "5.1",
            "population": "1420",
            "continent": "Asia",
        },
    ]

    sample_result = {"country": ["United States", "China"], "gdp": [23923.67, 17810.33]}
    sample_index = range(1, len(sample_result["country"]) + 1)

    result, index = average_gdp(sample_data)

    assert result["country"] == sample_result["country"]
    assert pytest.approx(result["gdp"]) == sample_result["gdp"]
    assert index == sample_index
