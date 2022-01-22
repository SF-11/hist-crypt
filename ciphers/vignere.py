"""
TODO
"""

from ciphers import caesar


def enc(text, key):
    """TODO
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


def dec(text, key):
    """TODO
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


def crack(text, key_length):
    """FIXME
    """
    split_texts = []
    
    for _ in range(key_length):
        split_texts.append("")

    idx = 0
    for letter in text:
        split_texts[idx] += letter
        idx = (idx + 1) % key_length

    split_plain = []

    for subtext in split_texts:
        shift_keys = caesar.eval_ciphertext(subtext)
        split_plain.append(caesar.shift(subtext, shift_keys[0]))

    plaintext = ""

    for j in range(len(split_plain[0])):
        for i in range(key_length):
            try:
                plaintext += split_plain[i][j]
            except IndexError:
                pass

    return plaintext
