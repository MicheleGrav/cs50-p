from fuel import convert, gauge
import pytest

# Test cases for the convert() function
def test_convert():
    assert convert("1/4") == 25
    assert convert("1/2") == 50
    assert convert("3/4") == 75

# Test cases for the gauge() function
def test_gauge():
    assert gauge(50) == "50%"
    assert gauge(1) == "E"
    assert gauge(99) == "F"

# Test ZeroDivisionError is raised
def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

# Test ValueError is raised for x > y
def test_value_error():
    with pytest.raises(ValueError):
        convert("5/3")
