to_convert = 1001
conv_val = {
    1: "I",
    5: "V",
    10: "X",
    50: "L",
    100: "C",
    500: "D",
    1000: "M"
}


def arabic_to_roman(conv):
    roman_number = ""
    if conv // 1000 >= 1:
        return roman_number.join(conv_val[1000]*(conv // 1000))


print(arabic_to_roman(to_convert))
