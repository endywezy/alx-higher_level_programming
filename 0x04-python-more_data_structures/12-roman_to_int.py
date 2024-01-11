#!/usr/bin/python3
# 12-roman_to_int.py

def roman_to_int(roman_string):
    """Converts a Roman numeral to an integer."""
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roman_dict = {
        "I": 1, "V": 5, "X": 10,
        "L": 50, "C": 100, "D": 500,
        "M": 1000
    }

    num = 0

    for i in range(len(roman_string)):
        current_value = roman_dict.get(roman_string[i], 0)

        if current_value == 0:
            return 0

        if i + 1 < len(roman_string):
            next_value = roman_dict.get(roman_string[i + 1], 0)

            if next_value == 0:
                return 0

            if current_value < next_value:
                num -= current_value
            else:
                num += current_value
        else:
            num += current_value

    return num
