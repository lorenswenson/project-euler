"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
import numpy as np
import utils


def problem003():
    """ Implement Sieve of Eratosthenes"""
    num = 600851475143
    # only need to check up to sqrt of num.... big savings on memory
    primes = utils.primes_below(int(np.ceil(np.sqrt(num))))
    remainder = num
    prime_factors = []
    for prime in np.nditer(primes):
        if prime == 0 or prime == 1:
            continue
        if remainder % prime == 0:
            # print(prime)
            prime_factors.append(prime)
            remainder = remainder / prime
        if remainder in primes:
            prime_factors.append(remainder)
            break
    print(prime_factors)


if __name__ == "__main__":
    problem003()
