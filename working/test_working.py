import pytest
from working import convert

def test_convert_valid_times():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("12:30 PM to 1:15 AM") == "12:30 to 01:15"

def test_convert_edge_cases():
    assert convert("12 AM to 1 AM") == "00:00 to 01:00"
    assert convert("12 PM to 1 PM") == "12:00 to 13:00"
    assert convert("1:00 PM to 1:00 AM") == "13:00 to 01:00"

def test_convert_invalid_times():
    with pytest.raises(ValueError):
        convert("8:60 AM to 4:60 PM")
    with pytest.raises(ValueError):
        convert("9:00 AM 5:00 PM")

def test_convert_no_minutes():
    assert convert("8 AM to 4 PM") == "08:00 to 16:00"
    assert convert("1 PM to 3 AM") == "13:00 to 03:00"
    assert convert("12 PM to 12 AM") == "12:00 to 00:00"

def test_convert_with_mixed_formats():
    assert convert("9:30 AM to 5 PM") == "09:30 to 17:00"
    assert convert("10 PM to 11:45 AM") == "22:00 to 11:45"
    assert convert("6:15 AM to 8:45 PM") == "06:15 to 20:45"
