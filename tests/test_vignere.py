import pytest
from ciphers import vignere



def test_encrypt():
    plaintext ="ATTACKATDAWN"
    key = "LEMON"
    assert vignere.encrypt(plaintext, key) == "LXFOPVEFRNHR"



def test_decrypt():
    ciphertext ="LXFOPVEFRNHR"
    key = "LEMON"
    assert vignere.decrypt(ciphertext, key) == "ATTACKATDAWN"



def test_encypt_1():
    """
    Test w/ keylength of 1, should be identical to a shift of 1
    """
    plaintext = "ABCDEFG"
    key = "B"
    assert vignere.encrypt(plaintext, key) == "BCDEFGH"



def test_decrypt_1():
    """
    Test w/ keylength of 1, should be identical to a shift of 1
    """
    plaintext = "BCDEFGH"
    key = "B"
    assert vignere.decrypt(plaintext, key) == "ABCDEFG"



def test_non_alpha_text():
    """
    """

    plaintext = "ATTACK AT DAWN"
    key = "LEMON"
    assert vignere.encrypt(plaintext, key) == "LXFOPV EF RNHR"
    assert vignere.decrypt("LXFOPV EF RNHR", key) == plaintext



def test_non_alpha_key():
    with pytest.raises(ValueError):
        vignere.encrypt("ATTACKATDAWN", "LEMON MELON")



def test_non_cap_text():
    """
    """
    plaintext = "attackatdawn"
    key = "LEMON"
    assert vignere.encrypt(plaintext, key) == "LXFOPVEFRNHR"
    assert vignere.decrypt("LXFOPVEFRNHR".lower(), key) == plaintext.upper()


def test_non_cap_key():
    """
    """
    plaintext = "ATTACKATDAWN"
    key = "lemon"
    assert vignere.encrypt(plaintext, key) == "LXFOPVEFRNHR"
    assert vignere.decrypt("LXFOPVEFRNHR".lower(), key) == plaintext