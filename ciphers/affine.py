"""
TODO
"""
from utils import num


def encrypt(text, a, b):
    """TODO
    """
    ciphertext = ""

    for letter in text:
        if letter.isalpha():
            ciphertext += chr(((((ord(letter)-65) * a) + b) % 26) + 65)
        else:
            ciphertext += letter

    return ciphertext


def decrypt(text, a, b):
    """TODO
    """
    plaintext = ""
    a_1 = num.modular_inverse(a, 26)

    for letter in text:
        if letter.isalpha():
            plaintext += chr(((((ord(letter) - 65) - b) * a_1) % 26) + 65)
        else:
            plaintext += letter

    return plaintext

# TODO input validation
