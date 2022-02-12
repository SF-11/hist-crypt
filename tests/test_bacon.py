import ciphers.bacon


def test_encrypt():
    secret = "HELP"
    message = "abcdefghijklmnopqrst"
    expected = "abCDEfgHijkLmNopQRSt"
    assert ciphers.bacon.encrypt(secret, message+"uvwxyz").startswith(expected)


def test_encrypt_unique():
    secret = "HELP"
    message = "abcdefghijklmnopqrst"
    expected = "abCDEfgHijkLmNOpQRST"
    assert ciphers.bacon.encrypt(secret, message+"uvwxyz", unique=True).startswith(expected)


def test_encrypt_nonalpha_secret():
    secret = " &^! "
    message = "abcdefghijklmnopqrst"
    try:
        ciphers.bacon.encrypt(secret, message+"uvwxyz", unique=True)
        assert False
    except ValueError:
        assert True


def test_encrypt_lowercase_secret():
    secret = "help"
    message = "abcdefghijklmnopqrst"
    expected = "abCDEfgHijkLmNopQRSt"
    assert ciphers.bacon.encrypt(secret, message+"uvwxyz").startswith(expected)


def test_encrypt_nonalpha_message():
    secret = "HELP"
    message = "abc! @def #ghi $jkl _mno (pqr) st."
    expected = "abC! @DEf #gHi $jkL _mNo (pQR) St."
    assert ciphers.bacon.encrypt(secret, message+"uvwxyz").startswith(expected)


def test_encrypt_message_too_short():
    secret = "HELP"
    message = "abcdefghijklmnopqrs"
    try:
        ciphers.bacon.encrypt(secret, message)
        assert False
    except ValueError:
        assert True


def test_encrypt_ab():
    secret = "HELP"
    assert ciphers.bacon.encrypt(secret) == "aabbbaabaaababaabbba"


def test_decrypt():
    message = "abCDEfgHijkLmNopQRStUVWXYZ"
    expected = "HELP"
    assert ciphers.bacon.decrypt(message).startswith(expected)


def test_decrypt_unique():
    message = "abCDEfgHijkLmNOpQRST"
    expected = "HELP"
    assert ciphers.bacon.decrypt(message+"uvwxyz", unique=True).startswith(expected)


def test_decrypt_nonalpha_message():
    message = "abC! @DEf #gHi $jkL _mNo (pQR) St."
    expected = "HELP"
    assert ciphers.bacon.decrypt(message+"uvwxyz").startswith(expected)

