from solutions.roman_to_integer import roman_to_integer


def test_romain_to_integer():

    # Trivial
    test_0, ref_test_0 = 'I', 1
    test_1, ref_test_1 = 'V', 5
    test_2, ref_test_2 = 'X', 10
    test_3, ref_test_3 = 'L', 50
    test_4, ref_test_4 = 'C', 100
    test_5, ref_test_5 = 'D', 500
    test_6, ref_test_6 = 'M', 1000

    # Basic
    test_7, ref_test_7 = 'III', 3
    test_8, ref_test_8 = 'LVIII', 58

    # Advanced
    test_8, ref_test_8 = 'MCMXCIV', 1994
    test_9, ref_test_9 = 'MDCCLXXVI', 1776

    assert roman_to_integer(test_0) == ref_test_0
    assert roman_to_integer(test_1) == ref_test_1
    assert roman_to_integer(test_2) == ref_test_2
    assert roman_to_integer(test_3) == ref_test_3
    assert roman_to_integer(test_4) == ref_test_4
    assert roman_to_integer(test_5) == ref_test_5
    assert roman_to_integer(test_6) == ref_test_6
    assert roman_to_integer(test_7) == ref_test_7
    assert roman_to_integer(test_8) == ref_test_8
    assert roman_to_integer(test_9) == ref_test_9


if __name__ == '__main__':
    test_romain_to_integer()
