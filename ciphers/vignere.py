from ciphers import caesar


def encrypt(text, key):
    """encrypt the text using the Vignere cipher

    Args:
        text (str): text to encrypt
        key (str): keyword to use for polyalphabetic shifting

    Raises:
        ValueError: TODO

    Returns:
        str: ciphertext
    """
    if not key.isalpha():
        raise ValueError("Key must contain letters only")

    text = text.upper()
    key = key.upper()
    key_idx = 0
    cipher = ""

    for letter in text:

        if not letter.isalpha():
            cipher += letter
            continue

        # TODO use shift util function
        cipher += chr((((ord(letter)-65) + (ord(key[key_idx])-65)) % 26) + 65)
        key_idx = (key_idx + 1) % len(key)

    return cipher


def decrypt(text, key):
    """decrypt the text using the Vignere cipher

    Args:
        text (str): text to decrypt
        key (str): keyword to use for polyalphabetic shifting

    Raises:
        ValueError: TODO

    Returns:
        str: plaintext
    """
    if not key.isalpha():
        raise ValueError("Key must contain letters only")

    text = text.upper()
    key = key.upper()
    key_idx = 0
    cipher = ""

    for letter in text:

        if not letter.isalpha():
            cipher += letter
            continue

        cipher += chr((((ord(letter)-65) - (ord(key[key_idx])-65)) % 26) + 65)
        key_idx = (key_idx + 1) % len(key)

    return cipher

