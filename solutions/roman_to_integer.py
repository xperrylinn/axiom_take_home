# Given a string representing a Roman numeral, write a function to compute the Arabic numerical equivalent.
# For example roman_to_arabic("MDCCLXXVI") should return 1776.


def roman_to_integer(s: str) -> int:
    # Assumptions:
    #   1 <= s.length <= 15
    #   s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
    #   It is guaranteed that s is a valid roman numeral in the range [1, 3999].

    # creating mapping from char to int
    r_to_i = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    # convert s to list type
    r_char_list = list(s)

    # map each char to int
    r_char_list = [r_to_i[r_char] for r_char in r_char_list]

    # process elem left to right, at i check i + 1 for exception
    for i in range(0, len(r_char_list) - 1):
        if r_char_list[i] < r_char_list[i + 1]:
            r_char_list[i + 1] = r_char_list[i + 1] - r_char_list[i]
            r_char_list[i] = 0

    # sum list, return result
    i_from_r = sum(r_char_list)

    return i_from_r
