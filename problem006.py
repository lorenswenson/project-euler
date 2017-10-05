"""
The sum of the squares of the first ten natural numbers is,
12 + 22 + ... + 102 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)2 = 552 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

import numpy as np


def problem006():
    sum_of_square = 0
    sum = 0
    for n in range(101):
        sum += n
        sum_of_square += n**2
    print(sum_of_square - sum**2)


if __name__ == "__main__":
    problem006()
