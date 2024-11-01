import pytest
from um import count

def test_count_basic():
    assert count("hello, um, world") == 1
    assert count("this is um, not yum") == 1

def test_count_word_boundaries():
    assert count("hum drum") == 0
    assert count("dummy") == 0

def test_count_case_insensitive():
    assert count("UM") == 1

def test_count_empty_string():
    assert count("") == 0

def test_count_multiple_spaces():
    assert count("um     um     um") == 3
    assert count("    um") == 1
    assert count("um    ") == 1

if __name__ == "__main__":
    pytest.main()
