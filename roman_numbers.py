from functools import wraps

to_convert = 989
conv_val = {
    1: "I",
    5: "V",
    10: "X",
    50: "L",
    100: "C",
    500: "D",
    1000: "M"
}

ROMAN_INPUT = "IVXLCDM"

conv_list = [1, 5, 10, 50, 100, 500, 1000]


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
            roman_number += conv_val[n] * k
            conv += - k * n

        if n > conv >= n - 1 and n != 1 and conv < 49:
            roman_number += conv_val[conv_list[0]] + conv_val[n]
            conv += - n + 1

        if n > conv >= n - 10 and n != 10 and 50 < n <= 100:
            roman_number += conv_val[conv_list[2]] + conv_val[n]
            conv += - n + 10

        if n > conv >= n - 100 and n != 100 and n > 100:
            roman_number += conv_val[conv_list[4]] + conv_val[n]
            conv += - n + 100

    return roman_number, conv


def roman_to_arabic(inp):
    return 1

if __name__ == "__main__":
    print(arabic_to_roman(to_convert))
    print(check_input("VX"))