from functools import wraps
from itertools import tee, zip_longest

to_convert = 989
conv_val_arab = {
    1: "I",
    5: "V",
    10: "X",
    50: "L",
    100: "C",
    500: "D",
    1000: "M"
}

conv_val_roman = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}

ROMAN_INPUT = "IVXLCDM"

conv_list = [1, 5, 10, 50, 100, 500, 1000]


def pairwise(iterable):
    a, b = tee(iterable)
    return zip_longest(a, b, fillvalue=next(b, None))


def check_input(inp):
    if type(inp) == int:
        return arabic_to_roman(inp)
    if type(inp) == str:
        if not set(inp) <= set(ROMAN_INPUT):
            raise ValueError('Illegal symbol')
        else:
            return roman_to_arabic(inp)
    else:
        raise ValueError('Illegal input')


def validate_input(func):
    @wraps(func)
    def wrapper(inp):
        if inp >= 4000:
            raise ValueError('Input too large')
        if inp <= 0:
            raise ValueError('Input too small')
        return func(inp)

    return wrapper


@validate_input
def arabic_to_roman(conv):
    roman_number = ""
    for n in reversed(conv_list):
        if conv // n >= 1:
            k = conv // n
            roman_number += conv_val_arab[n] * k
            conv += - k * n

        if n > conv >= n - 1 and n != 1 and conv < 49:
            roman_number += conv_val_arab[conv_list[0]] + conv_val_arab[n]
            conv += - n + 1

        if n > conv >= n - 10 and n != 10 and 50 < n <= 100:
            roman_number += conv_val_arab[conv_list[2]] + conv_val_arab[n]
            conv += - n + 10

        if n > conv >= n - 100 and n != 100 and n > 100:
            roman_number += conv_val_arab[conv_list[4]] + conv_val_arab[n]
            conv += - n + 100

    return roman_number, conv


def roman_to_arabic(inp):
    roman_number = 0
    nex = False
    for s_1, s_2 in pairwise(inp):
        if nex:
            nex = False
            continue
        if s_1 == "I" and (s_2 == "X" or s_2 == "V"):
            roman_number += conv_val_roman[s_2] - 1
            nex = True
            continue
        if s_1 == "X" and (s_2 == "L" or s_2 == "C"):
            roman_number += conv_val_roman[s_2] - 10
            nex = True
            continue
        if s_1 == "C" and (s_2 == "D" or s_2 == "M"):
            roman_number += conv_val_roman[s_2] - 100
            nex = True
            continue
        if s_1 == "I" or s_1 == "X" or s_1 == "C" or s_1 == "M":
            roman_number += conv_val_roman[s_1]

    return roman_number, inp


if __name__ == "__main__":
    print(arabic_to_roman(to_convert))
    print(check_input("XCIX"))
