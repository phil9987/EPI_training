from test_framework import generic_test
from test_framework.test_failure import TestFailure


def int_to_string(x):
    res = ''
    is_neg = False
    if x < 0:
        is_neg = True
        x *= (-1)
    elif x == 0:
        return '0'
    while x > 0:
        curr_digit = x % 10
        x = x // 10
        res += chr(ord('0') + curr_digit)
    if is_neg:
        res += '-'
    return res[::-1]

def char_to_int(c):
    return ord(c) - ord('0')

def string_to_int(s):
    if not s:
        return 0
    is_neg = True if s[0] == '-' else False
    if is_neg:
        s = s[1:]
    base = 1
    res = 0
    for c in s[::-1]:
        res += (base * char_to_int(c))
        base *= 10
    if is_neg:
        return -res
    else:
        return res

def wrapper(x, s):
    if int_to_string(x) != s:
        raise TestFailure("Int to string conversion failed")
    if string_to_int(s) != x:
        raise TestFailure("String to int conversion failed")


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("string_integer_interconversion.py",
                                       'string_integer_interconversion.tsv',
                                       wrapper))
