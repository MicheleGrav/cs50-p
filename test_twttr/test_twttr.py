from twttr import shorten

# Check for inputs with a single word
def test_single():
    assert shorten("hello") == "hll"
    assert shorten("Hi") == "H" # Uppercase inputs variation

# Check for inputs with multiple words
def test_multiple():
    assert shorten("this is nice") == "ths s nc"
    assert shorten("Is iT alReady nOoN?") == "s T lRdy nN?" # Uppercase inputs variation

# Check for inputs that have digits
def test_digits():
    assert shorten("CS50") == "CS50"
    assert shorten("12ab48") == "12b48"

# Check for inputs with varied punctuation
def test_punctuation():
    assert shorten("Hi, this is cool") == "H, ths s cl"
    assert shorten("Well! This is, really... sweet") == "Wll! Ths s, rlly... swt"
