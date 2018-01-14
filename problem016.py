"""
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

 What is the sum of the digits of the number 2^1000?
"""


def problem16(n):
    acc = 0
    for s in str(2**n):
        acc += int(s)
    return acc


if __name__ == '__main__':
    print(problem16(1000))
