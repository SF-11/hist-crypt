import pytest
from ciphers import vignere



def test_encrypt():
    plaintext ="ATTACKATDAWN"
    key = "LEMON"
    assert vignere.enc(plaintext, key) == "LXFOPVEFRNHR"



def test_decrypt():
    ciphertext ="LXFOPVEFRNHR"
    key = "LEMON"
    assert vignere.dec(ciphertext, key) == "ATTACKATDAWN"



def test_encypt_1():
    """
    Test w/ keylength of 1, should be identical to a shift of 1
    """
    plaintext = "ABCDEFG"
    key = "B"
    assert vignere.enc(plaintext, key) == "BCDEFGH"



def test_decrypt_1():
    """
    Test w/ keylength of 1, should be identical to a shift of 1
    """
    plaintext = "BCDEFGH"
    key = "B"
    assert vignere.dec(plaintext, key) == "ABCDEFG"



def test_non_alpha_text():
    """
    """

    plaintext = "ATTACK AT DAWN"
    key = "LEMON"
    assert vignere.enc(plaintext, key) == "LXFOPV EF RNHR"
    assert vignere.dec("LXFOPV EF RNHR", key) == plaintext



def test_non_alpha_key():
    with pytest.raises(ValueError):
        vignere.enc("ATTACKATDAWN", "LEMON MELON")



def test_non_cap_text():
    """
    """
    plaintext = "attackatdawn"
    key = "LEMON"
    assert vignere.enc(plaintext, key) == "LXFOPVEFRNHR"
    assert vignere.dec("LXFOPVEFRNHR".lower(), key) == plaintext.upper()


def test_non_cap_key():
    """
    """
    plaintext = "ATTACKATDAWN"
    key = "lemon"
    assert vignere.enc(plaintext, key) == "LXFOPVEFRNHR"
    assert vignere.dec("LXFOPVEFRNHR".lower(), key) == plaintext