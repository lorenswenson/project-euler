"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

"""

import numpy as np


def check_palinedrome(num):
    str_num = str(int(num))
    midpoint = int(np.floor(len(str_num) / 2))
    for ind in range(midpoint):
        if str_num[ind] != str_num[(-ind) - 1]:
            return False
    return True


def get_palindromes():
    # Largest num is up to 1e6
    for n in range(int(1e6), 2, -1):
        if check_palinedrome(n):
            yield n


def find_factors(num):
    factors = []
    for n in range(2, 999, 1):
        if num % n == 0 and num / n < 1000:
            factors.append((n, int(num / n)))
    return factors


def problem004():
    for p in get_palindromes():
        factors = find_factors(p)
        if len(factors) > 0:
            print("{}: {}".format(p, factors))
            break


if __name__ == "__main__":
    problem004()
