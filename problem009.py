"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a**2 + b**2 = c**2

For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""


def problem():

    for a in range(1000):
        for b in range(a + 1, 1000):
            if a + b + (a**2 + b**2) ** (1 / 2) == 1000:
                print("{}, {}, abc: {}".format(
                    a, b, a * b * (a**2 + b**2)**(1 / 2)))


if __name__ == "__main__":
    problem()
