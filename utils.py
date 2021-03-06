
import functools
import numpy as np


def num_to_index(p):
    """Array represents odd numbers starting from 3.  
Find index corresponding to odd p."""
    return int((p - 1) / 2 - 1)


def index_to_num(ind):
    """Find the corresponding prime for an index into 
an array of odd numbers starting from 3."""
    return int((ind + 1) * 2 + 1)


def primes_below(num):
    """Implement Sieve of Eratosthenes to find a list of primes below NUM"""
    sqrt_num = int(np.ceil(np.sqrt(num)))
    # Only consider odd numbers for space saving
    if num % 2 == 0:
        array_size = int(num / 2 - 1)
    else:
        array_size = int((num - 1) / 2 - 1)
    touched = np.zeros(array_size)  # only worry about odd numbers >= 3
    current_prime = 3
    while True:
        if current_prime >= sqrt_num:
            break
        # Start at current_prime**2 for significant time savings
        p = current_prime**2
        while p < num:
            if p % 2 != 0:
                touched[num_to_index(p)] = 1
            p += current_prime

        ind = num_to_index(current_prime)
        while index_to_num(ind) <= sqrt_num:
            ind += 1
            if touched[ind] == 0:
                break
        current_prime = index_to_num(ind)

    return np.array([index_to_num(n) for n in np.nditer(np.nonzero(touched == 0)[0])])


def find_factors(num):
    """Finds all factors of num (including 1 and num).  Only needs 
to check up to sqrt(num) as the matching factor will be above this number."""
    factors = []
    for n in range(1, int(np.round(np.sqrt(num))) + 1):
        if num % n == 0:
            factors.append(n)
            if num / n != n:
                factors.append(int(num / n))
    return factors


def get_triangle_number(num):
    """Calculate 1+2+...+num"""
    return functools.reduce(lambda x, y: x + y, range(num + 1))
