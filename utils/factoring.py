"""
file: factoring.py
author: Scott F
date: 2/22/18

Provides functionality to factor numbers using the
pollard-rho algorithm. There are two variations:
the standard pollard-rho, and one that uses an
accumulator to improve runtime.
"""

import math
from primes import get_prime


def _p_r_factor_helper(x):
    """
    function used in the pollard-rho factorization algorithm
    """
    return (x * x) + 1


def pollard_rho_factor(n, x1=1):
    """
    Using the pollard rho factoring algorithm, this
    algorithm computes a factor of n. To get the 
    other one, simply do q = n/p.

    :param n: the number we are factoring
    :param x1: initial value, defaulted to 1

    :returns: a factor of n or -1 if it fails
    """
    x = x1
    xx = _p_r_factor_helper(x) % n
    p = math.gcd(x - xx, n)
    count = 1  # used to count iterations for problem 5.26
    while p == 1:
        x = _p_r_factor_helper(x) % n
        xx = _p_r_factor_helper(xx) % n
        xx = _p_r_factor_helper(xx) % n
        p = math.gcd(x - xx, n)
        count += 1

    if p == n:
        return -1, count
    else:
        return p, count


def pollard_rho_factor_accum(n, x1=1, k=100):
    """
    This is a variation of the pollard rho factoring 
    algorithm, which makes use of an accumulator to
    improve efficiency. 

    :param n: the number we are factoring
    :param x1: initial value, defaulted to 1
    :param k:

    :returns: a factor of n or -1 if it fails
    """
    x = x1
    xx = _p_r_factor_helper(x) % n
    count = 1
    z = 1
    p = math.gcd(x - xx, n)
    while p == 1:
        x = _p_r_factor_helper(x) % n
        xx = _p_r_factor_helper(xx) % n
        xx = _p_r_factor_helper(xx) % n

        z = (z * (x - xx)) % n
        count += 1

        if count % k == 0:
            p = math.gcd(z, n)

            if 1 < p < n:
                return p

            z = 1

    if p == n:
        return -1
    else:
        return p


def get_RSA_modulus(b, num):
    """
    Generates a list of RSA modulus' of bit length b
    such that each modulus, n = pq, where p and q are
    both primes.

    :param b: bit length of the modulus
    :param num: number of modulus' you want

    :returns: a list of RSA modulus'
    """
    p_lst = []

    # generate primes of length b/2 because when we multiply 2 together, the length
    # will be b-bits long
    for _ in range(0, num + 1):
        p_lst.append(get_prime(b // 2))

    n_list = []
    for i in range(0, num):
        n_list.append(p_lst[i] * p_lst[i + 1])

    return n_list
