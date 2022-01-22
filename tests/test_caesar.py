import pytest
from ciphers import caesar



def test_encrypt_rot1():
    plaintext = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    shift_key = 1

    assert caesar.shift(plaintext, shift_key) == "BCDEFGHIJKLMNOPQRSTUVWXYZA"


def test_decrypt_rot1():
    ciphertext = "BCDEFGHIJKLMNOPQRSTUVWXYZA"
    shift_key = -1

    assert caesar.shift(ciphertext, shift_key) == "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def test_encrypt_rot25():
    plaintext = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    shift_key = 25

    assert caesar.shift(plaintext, shift_key) == "ZABCDEFGHIJKLMNOPQRSTUVWXY"



def test_decrypt_rot25():
    ciphertext = "ZABCDEFGHIJKLMNOPQRSTUVWXY"
    shift_key = -25

    assert caesar.shift(ciphertext, shift_key) == "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def test_non_cap_text():
    plaintext = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".lower()
    shift_key = 1

    assert caesar.shift(plaintext, shift_key) == "BCDEFGHIJKLMNOPQRSTUVWXYZA"
    assert caesar.shift("BCDEFGHIJKLMNOPQRSTUVWXYZA".lower(), -1 * shift_key) == plaintext.upper()




def test_non_int_key():
    with pytest.raises(ValueError):
        caesar.shift("ABCDEFG", "A")



def test_non_alpha_text():
    plaintext = "ABC DEF_GHI+JKL\\MNO/PQR!STU#VWX%YZ"
    shift_key = 1

    assert caesar.shift(plaintext, shift_key) == "BCD EFG_HIJ+KLM\\NOP/QRS!TUV#WXY%ZA"


