"""
file: primes.py
author: Scott F
date: 2/22/18

Provides functionality to generate both regular and RSA-safe primes.
"""
import random


def get_prime(b):
    """
    generates a prime number with a specified number of bits

    :param b: number of bits in the prime number

    :returns: a prime number of b bits
    """
    num = -1
    check = False
    while not check:
        num = random.getrandbits(b)
        check = rabin_miller(num, 5)

    return num


def get_RSA_prime(b):
    """
     Generates an RSA safe prime p such that 
     p = 2s + 1, where s is also prime

    :param b: number of bits in the prime number

    :returns: an RSA-safe prime of b bits
    """
    while True:
        # get base prime, s
        s = random.getrandbits(b)

        # don't bother checking even nums
        if s & 1 == 0:
            continue

        if rabin_miller(s, 5):
            # verify this generates an RSA safe prime
            p = (2 * s) + 1
            if rabin_miller(p, 5):
                return p


def rabin_miller(n, k=1):
    """
    param n: the number that we are checking for primality
    param k: the number of times we want to check the number, n

    Preforms the Rabin-Miller algorithm to determine whether or not
    a number is prime

    return True if n is probably prime, False if n is composite
    """
    if n < 5:  # FIXME
        return False

    # break down n-1 into (2^r)*d
    d = n - 1
    r = 0
    while d & 1 == 0:
        d = d // 2
        r += 1

    for i in range(0, k):
        broken = False
        a = random.randint(2, n - 2)
        x = pow(a, d, n)

        if x == 1 or x == n - 1:
            continue

        for j in range(0, r - 1):
            x = pow(x, 2, n)
            if x == 1:
                return False  # composite
            if x == n - 1:
                broken = True
                break

        if not broken:
            return False  # composite

    return True  # probably prime
