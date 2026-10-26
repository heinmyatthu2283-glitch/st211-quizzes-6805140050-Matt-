import pytest
from roman import convert


# Category 1: Single Symbols
def test_single_symbols():
    assert convert("I") == 1
    assert convert("V") == 5
    assert convert("X") == 10
    assert convert("L") == 50
    assert convert("C") == 100
    assert convert("D") == 500
    assert convert("M") == 1000


# Category 2: Repeated Symbols
def test_repeated_symbols():
    assert convert("II") == 2
    assert convert("III") == 3
    assert convert("XX") == 20


# Category 3: Additive Notation
def test_additive_notation():
    assert convert("VI") == 6
    assert convert("XVI") == 16
    assert convert("CLVII") == 157


# Category 4: Subtractive Notation
def test_subtractive_notation():
    assert convert("IV") == 4
    assert convert("IX") == 9
    assert convert("XL") == 40
    assert convert("XC") == 90
    assert convert("CD") == 400
    assert convert("CM") == 900


# Category 5: Mixed Additive & Subtractive Notation
def test_mixed_notation():
    assert convert("XIX") == 19
    assert convert("LVIII") == 58
    assert convert("MCMXCIV") == 1994


# Category 6: Invalid Input
def test_invalid_input():
    with pytest.raises(ValueError):
        convert("ABC")

    with pytest.raises(ValueError):
        convert("")

    with pytest.raises(ValueError):
        convert("VX")

    with pytest.raises(ValueError):
        convert("XXC")

    with pytest.raises(ValueError):
        convert("IIII")

    with pytest.raises(ValueError):
        convert("VV")