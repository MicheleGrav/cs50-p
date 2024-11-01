import pytest
from numb3rs import validate

def test_valid_ipv4_addresses():
    assert validate("192.168.1.1") == True
    assert validate("0.0.0.0") == True
    assert validate("100.100.100.100") == True

def test_invalid_ipv4_addresses():
    assert validate("256.256.256.256") == False
    assert validate("192.168.1.256") == False
    assert validate("abc.def.ghi.jkl") == False

def test_edge_cases():
    assert validate("1.1.1.1") == True
    assert validate("01.01.01.01") == True
    assert validate("0.0.0.0") == True
    assert validate("255.0.255.255") == True
    assert validate("0.255.255.255") == True

if __name__ == "__main__":
    pytest.main()
