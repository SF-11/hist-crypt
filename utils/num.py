"""
TODO
"""


def is_residue(a, p):
    """
    :param a: number to check for residuality
    :param p: prime modulus
    :returns: true if it is a quadratic residue, false otherwise

    uses euler criterion to determine if a is quadratic residue mod p
    """
    n = exponentiate(a, (p - 1) // 2, p)
    if n == 1:
        return True
    else:
        return False


def square_root(n, p):
    """
    find sqrt(n) % p through brute force
    """
    for i in range(1, p):
        if exponentiate(i, 2, p) == n:
            return i

    return -1


def gcd(a, b):
    """
    Euclidean alg
    """
    r = {0: a, 1: b}  # remainders
    q = {}  # quotients
    m = 1
    while r[m] != 0:
        q[m] = r[m - 1] // r[m]
        r[m + 1] = r[m - 1] - (q[m] * r[m])
        m += 1
    m -= 1
    return r[m]


def exponentiate(base, exp, p):
    """
    uses the square and multiply algorithm to 
    get (base^exp)%p

    :param base: base of the exponentiation
    :param exp: power that the base is being raised to
    :param p: prime modulus 

    :returns: (base^exp) mod p
    """
    e = "{0:b}".format(exp)  # bitstring of the exponent

    z = 1
    for c in e:
        z = z * z % p

        if int(c) == 1:
            z = z * base % p
    return z


def modular_inverse(n, p):
    """
    invert n mod p using extended euclid algorithm
    
    the algorithm breaks down into:
    gcd(n,p) = s*p + t*n
    since s*p % p is 0, we have that t%p = n^-1

    :param n: number to invert, b
    :param p: prime modulus, a
    
    :returns: n^-1 mod p
    """
    p0 = p  # local copy of original prime modulus
    n0 = n  # local copy of original number being inverted

    # initial breakdown
    t0 = 0
    t = 1
    q = int(p0 / n0)  # initial quotient of p and n
    r = p0 - (q * n0)

    # continue breaking down
    while r > 0:
        temp = (t0 - (q * t)) % p
        t0 = t
        t = temp
        p0 = n0
        n0 = r
        q = int(p0 / n0)
        r = p0 - (q * n0)

    # if n0 doesn't reach 1, n is not invertible
    if n0 != 1:
        return -1
    else:
        return t


def dec_to_tri(n):
    """
    :param n: decimal number to be converted to trinary
    :returns: trinary string of the number n
    """
    tri_string = ""

    while n != 0:
        tri_string = str(n % 3) + tri_string
        n = n // 3

    return tri_string


def tri_to_dec(n):
    """
    :param n: string representation of a trinary number
    :returns: decimal number for n
    """
    dec = 0
    m = len(n) - 1

    for char in n:
        dec += int(char) * (3 ** m)
        m -= 1

    return dec
