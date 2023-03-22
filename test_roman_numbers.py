import pytest
from roman_numbers import arabic_to_roman, check_input


def test_input():
    with pytest.raises(ValueError):
        arabic_to_roman(4000)
    assert check_input("IX") == (9, 'IX')
    assert check_input("XCIX") == (99, 'XCIX')

def test_arabic_numbers():
    assert arabic_to_roman(1501) == ("MDI", 0)


def test_complex():
    assert arabic_to_roman(9) == ("IX", 0)
    assert arabic_to_roman(99) == ("XCIX", 0)
    assert arabic_to_roman(90) == ("XC", 0)
    assert arabic_to_roman(900) == ("CM", 0)
    assert arabic_to_roman(989) == ("CMLXXXIX", 0)
    assert arabic_to_roman(3999) == ("MMMCMXCIX", 0)
    assert arabic_to_roman(3439) == ("MMMCDXXXIX", 0)
