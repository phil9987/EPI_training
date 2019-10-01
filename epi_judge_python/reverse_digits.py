from test_framework import generic_test


def reverse(x):
    res = 0
    isNeg = False
    if x < 0:
        isNeg = True
        x *= -1
    while x > 0:
        currDigit = x % 10
        x = x //10
        res *= 10
        res += currDigit
    if isNeg:
        res *= -1
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("reverse_digits.py",
                                       'reverse_digits.tsv', reverse))
