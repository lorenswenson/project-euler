
import numpy as np


def num_to_index(p):
    """Array represents odd numbers starting from 3.  Find index corresponding to odd p."""
    return int((p - 1) / 2 - 1)


def index_to_num(ind):
    """Find the corresponding prime for an index into an array of odd numbers starting from 3."""
    return int((ind + 1) * 2 + 1)


def primes_below(num):
    """Implement Sieve of Eratosthenes to find a list of primes below NUM"""
    sqrt_num = int(np.ceil(np.sqrt(num)))
    if num % 2 == 0:
        array_size = int(num / 2 - 1)
    else:
        array_size = int((num - 1) / 2 - 1)
    touched = np.zeros(array_size)  # only worry about odd numbers >= 3
    current_prime = 3
    while True:
        if current_prime >= sqrt_num:
            break
        # p = current_prime**2
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
