"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

"""

import numpy as np


def is_valid(num):
    for n in range(11, 21, 1):
        if num % n != 0:
            return False
    return True


def problem005():
    current = 1
    while True:
        if is_valid(current):
            print(current)
            break
        current += 1


if __name__ == "__main__":
    problem005()
