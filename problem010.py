"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

import numpy as np
import utils


def problem():
    primes = utils.primes_below(int(2e6))
    len(primes)
    sum = 0
    for prime in np.nditer(primes):
        sum = sum + prime
    print(sum)


if __name__ == "__main__":
    problem()
