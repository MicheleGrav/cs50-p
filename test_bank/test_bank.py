from bank import value

# Check for input "hello" case insensitively
def test_hello():
    assert value("hello") == 0
    assert value("hELLo people") == 0

# Check for input starting with 'h' but not hello
def test_hword():
    assert value("high five") == 20
    assert value("hhhappy birthday") == 20

# Check for input of other type
def test_other():
    assert value("0192") == 100
    assert value("184ah yes") == 100
