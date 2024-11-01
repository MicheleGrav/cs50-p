from seasons import parse_date, calc_mins, minutes_to_words
from datetime import date
import pytest

def test_parse_date():
    assert parse_date("2000-01-01") == date(2000, 1, 1)
    with pytest.raises(ValueError):
        parse_date("01-01-2000")
    with pytest.raises(ValueError):
        parse_date("2000/01/01")

def test_calculate_minutes():
    birth_date = date(2000, 1, 1)
    today = date(2024, 10, 28)
    days_difference = (today - birth_date).days
    expected_minutes = days_difference * 24 * 60
    assert calc_mins(birth_date) == expected_minutes

def test_convert_minutes_to_words():
    assert minutes_to_words(1000000) == "One million"
    assert minutes_to_words(12347) == "Twelve thousand, three hundred forty-seven"
