"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

"""

import numpy as np


def solution():
    goal = 10001
    primes = [2, 3, 5]
    current = 7
    while True:
        passed = True
        for p in primes:
            if current % p == 0:
                passed = False
                break
        if passed == True:
            primes.append(current)
        current += 2
        if len(primes) == goal:
            break
    print(primes[-1])


if __name__ == "__main__":
    solution()
