from functools import wraps

to_convert = 1501
conv_val = {
    1: "I",
    5: "V",
    10: "X",
    50: "L",
    100: "C",
    500: "D",
    1000: "M"
}


def validate_input(func):
    @wraps(func)
    def wrapper(inp):
        if not type(inp) == int:
            raise ValueError('Illegal symbol')
        return func(inp)

    return wrapper


@validate_input
def arabic_to_roman(conv):
    roman_number = ""
    if conv // 1000 >= 1:
        k = conv // 1000
        roman_number += conv_val[1000] * k
        conv = conv - k * 1000
        print(roman_number)
    if conv // 500 >= 1:
        k = conv // 500
        roman_number += conv_val[500] * k
        conv = conv - k * 500
    return roman_number, conv


if __name__ == "__main__":
    print(arabic_to_roman(to_convert))
