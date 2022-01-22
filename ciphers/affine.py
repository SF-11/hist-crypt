from utils import num


def encrypt(text, a, b):
    """use the affine cipher to encrypt each char in the text as (char*a)+b

    Args:
        text (str): plaintext to encrypt
        a (int): a, such that (plaintext*a)+b %26 = ciphertext
        b (int): b, such that (plaintext*a)+b %26 = ciphertext

    Returns:
        string: ciphertext
    """
    ciphertext = ""

    for letter in text:
        if letter.isalpha():
            ciphertext += chr(((((ord(letter)-65) * a) + b) % 26) + 65)
        else:
            ciphertext += letter

    return ciphertext


def decrypt(text, a, b):
    """use the affine cipher to decrypt each char in the text as (char-b)*a^-1

    Args:
        text (str): ciphertext to decrypt
        a (int): a, such that (plaintext*a)+b %26 = ciphertext
        b (int): b, such that (plaintext*a)+b %26 = ciphertext

    Returns:
        str: plaintext
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
