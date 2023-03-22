import pytest
from roman_numbers import check_input


def test_input():
    with pytest.raises(ValueError):
        check_input(4000)


def test_roman():
    assert check_input("IX") == (9, 'IX')
    assert check_input("XCIX") == (99, 'XCIX')
    assert check_input("MMMCDXXXIX") == (3439, "MMMCDXXXIX")
    assert check_input("MMMCMXCIX") == (3999, "MMMCMXCIX")


def test_arabic():
    assert check_input(9) == ("IX", 0)
    assert check_input(99) == ("XCIX", 0)
    assert check_input(90) == ("XC", 0)
    assert check_input(900) == ("CM", 0)
    assert check_input(989) == ("CMLXXXIX", 0)
    assert check_input(3999) == ("MMMCMXCIX", 0)
    assert check_input(3439) == ("MMMCDXXXIX", 0)
