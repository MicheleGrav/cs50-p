from plates import is_valid

def test_valid():
    assert is_valid("CS50") is True  # Valid plate with letters and numbers at the end
    assert is_valid("HELLO") is True  # Valid plate with only letters
    assert is_valid("AB123") is True  # Valid plate with letters followed by numbers
    assert is_valid("XYZ99") is True  # Valid plate with letters followed by two numbers
    assert is_valid("PLATE") is True  # Valid plate with only letters

def test_invalid():
    assert is_valid("CS05") is False  # Invalid: starts with a leading zero in the numbers
    assert is_valid("OUTATIME") is False  # Invalid: too many characters (more than 6)
    assert is_valid("A") is False  # Invalid: too few characters (less than 2)
    assert is_valid("AAA22A") is False  # Invalid: letters after numbers
    assert is_valid("12345") is False  # Invalid: does not start with letters
    assert is_valid("AB123#") is False  # Invalid: contains non-alphanumeric character
    assert is_valid("AB 123") is False  # Invalid: contains a space
    assert is_valid("AB0123") is False  # Invalid: starts with 0 after letters
    assert is_valid("A1") is False  # Invalid: too few characters and number after one letter

