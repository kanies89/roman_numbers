import pytest
from roman_numbers import arabic_to_roman


def test_arabic_input():
    with pytest.raises(ValueError):
        arabic_to_roman("arabic_number")
