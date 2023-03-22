from functools import wraps

to_convert = 90
conv_val = {
    1: "I",
    5: "V",
    10: "X",
    50: "L",
    100: "C",
    500: "D",
    1000: "M"
}

conv_list = [1, 5, 10, 50, 100, 500, 1000]


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
    for n in reversed(conv_list):
        if conv == n - 1 and n != 1:
            roman_number += conv_val[conv_list[0]] + conv_val[n]
            conv = conv - n + 1

        if conv == n - 10 and n != 10:
            roman_number += conv_val[conv_list[2]] + conv_val[n]
            conv = conv - n + 10

        if conv // n >= 1:
            k = conv // n
            roman_number += conv_val[n] * k
            conv = conv - k * n

    return roman_number, conv


if __name__ == "__main__":
    print(arabic_to_roman(to_convert))
