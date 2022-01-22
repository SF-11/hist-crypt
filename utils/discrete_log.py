"""
file: discrete_log.py
author: Scott F
date: 2/22/18

Provides functionality to take discrete logs using the 
pollard-rho algorithm. When run directly, this solves
problem 6.3 in the Stinson cryptography book.
"""

from math import sqrt, gcd
from typing import List

from utils.num import exponentiate, modular_inverse


def prime_factors(n):
    """
    Finds all of the prime factors of n
    
    :param n: the number you want the factorization of

    :returns: a list containing all of the prime factors of n
    """
    factors = []
    while n & 1 == 0:
        factors.append(2)
        n = n // 2

    for i in range(3, int(sqrt(n)) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n = n // i

    if n > 2:
        factors.append(n)

    return factors


def find_primitive(n):
    """
    Finds the lowest primitive element of n, assuming
    that n is prime

    :param n: prime modulus you want to find primitive of
    
    :returns: lowest primitive element of n
    """
    phi = n - 1
    s = prime_factors(phi)

    for r in range(2, n):
        flag = False
        for i in s:
            if exponentiate(r, phi // i, n) == 1:
                flag = True
                break

        if not flag:
            return r


def order(alpha, p):
    """
    Determines the order of an element

    :param alpha: the element we want to find the order of
    :param p: the prime modulus

    :returns: the order of alpha
    """
    count = 1
    x = alpha
    while x != 1:
        x = (x * alpha) % p
        count += 1

    return count


def _p_r_log_helper(x, a, b, alpha, beta, n, p):
    """
    Step function used with the pollard rho discrete log algorithm
    """
    if x % 3 == 1:
        f = ((beta * x) % p, a, (b + 1) % n)
    elif x % 3 == 0:
        f = ((x * x) % p, (2 * a) % n, (2 * b) % n)
    else:
        f = ((alpha * x) % p, (a + 1) % n, b)
    return f


def pollard_rho_log(alpha, beta, p):
    """
    Finds the discrete log base alpha of beta

    :param alpha: base of the logarithm
    :param beta: alpha^a
    :param p: prime modulus

    :returns: log base alpha of beta
    """
    n = p - 1  # alpha is primitive
    # n = 57251   # for problem 6.3
    (x, a, b) = _p_r_log_helper(1, 0, 0, alpha, beta, n, p)
    (xx, aa, bb) = _p_r_log_helper(x, a, b, alpha, beta, n, p)
    while x != xx:
        (x, a, b) = _p_r_log_helper(x, a, b, alpha, beta, n, p)
        (xx, aa, bb) = _p_r_log_helper(xx, aa, bb, alpha, beta, n, p)
        (xx, aa, bb) = _p_r_log_helper(xx, aa, bb, alpha, beta, n, p)

    # solving for the log, c, can only be done trivially
    # if the gcd is 1. For the case that is is 2, we can
    # take advantage of the chinese remainder
    g = gcd(bb - b, n)
    if g == 2:
        s = n // 2

        p = 2
        q = s
        p_inv = (s + 1) // 2
        q_inv = 1

        b_inv = modular_inverse(bb - b, s)
        y = ((a - aa) * b_inv) % s

        x1 = 1
        x2 = 0
        c1 = ((x1 * q * q_inv) + (y * p * p_inv)) % n
        c2 = ((x2 * q * q_inv) + (y * p * p_inv)) % n
        return c1, c2

    elif g > 2:
        return -1, -1
    else:
        b_inv = modular_inverse(bb - b, n)
        return ((a - aa) * b_inv) % n, -1


def discrete_log_bruteforce(alpha, beta, p):
    """
    finds the value "a" in the relationship:
            alpha^a = beta (mod p) 
    using a naive method of checking each exponentiation

    :param alpha: base
    :param beta: base^a
    :param p: prime modulus

    :returns: discrete log of beta
    """
    for i in range(1, p):
        alpha_i = exponentiate(alpha, i, p)
        if alpha_i == beta:
            return i
    return -1


def discrete_log_shanks(alpha, beta, p):
    """
    finds the value "a" in the relationship:
            alpha^a = beta (mod p) 
    using shank's algorithm

    :param alpha: base
    :param beta: base^a
    :param p: prime modulus

    :returns: discrete log of beta
    """
    m = int(sqrt(p)) + 1  # sqrt from math package

    d1 = {}
    am = exponentiate(alpha, m, p)
    for j in range(0, m):
        if j == 0:
            d1[j] = 1
        elif j == 1:
            d1[j] = am
        else:
            d1[j] = d1[j - 1] * am % p

    L1 = sorted(d1.items(), key=lambda x: x[1])  # type: List[(int, int)]

    d2 = {}
    for i in range(0, m):
        d2[i] = beta * modular_inverse(exponentiate(alpha, i, p), p) % p

    L2 = sorted(d2.items(), key=lambda x: x[1])  # type: List[(int, int)]

    # traverse through to find a match, in a "merge-like" fashion
    L1_idx = 0
    L2_idx = 0
    # iterate through both lists simultaneously
    while L1_idx < m and L2_idx < m:
        if L1[L1_idx][1] == L2[L2_idx][1]:
            return ((m * L1[L1_idx][0]) + L2[L2_idx][0]) % p

        elif L1[L1_idx][1] < L2[L2_idx][1]:
            L1_idx += 1

        else:
            L2_idx += 1

    # check remaining values from L1
    while L1_idx < m:
        if L1[L1_idx][1] == L2[L2_idx][1]:
            return ((m * L1_idx) + L2_idx) % p

        L1_idx += 1

    # check remaining values from L2
    while L2_idx < m:
        if L1[L1_idx][1] == L2[L2_idx][1]:
            return ((m * L1_idx) + L2_idx) % p

        L2_idx += 1

    # no discrete log
    return -1
