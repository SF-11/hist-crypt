import ciphers.adfgvx

alpha_5x5 = [
    ["b", "t", "a", "l", "p"],
    ["d", "h", "o", "z", "k"],
    ["q", "f", "v", "s", "n"],
    ["g", "ij", "c", "u", "x"],
    ["m", "r", "e", "w", "y"]
]


alpha_6x6 = [
    ["n", "a", "1", "c", "3", "h"],
    ["8", "t", "b", "2", "o", "m"],
    ["e", "5", "w", "r", "p", "d"],
    ["4", "f", "6", "g", "7", "i"],
    ["9", "j", "0", "k", "l", "q"],
    ["s", "u", "v", "x", "y", "z"]
]


def test_encrypt_5x5():
    plaintext = "ATTACKATONCE"
    trans_key = "CARGO"
    assert ciphers.adfgvx.encrypt(plaintext, trans_key, alpha_5x5) == "FAXDFADDDGDGFFFAFAXAFAFX"


def test_decrypt_5x5():
    ciphertext = "FAXDFADDDGDGFFFAFAXAFAFX"
    key = "CARGO"
    assert ciphers.adfgvx.decrypt(ciphertext, key, alpha_5x5) == "ATTACKATONCE"


def test_encrypt_6x6():
    plaintext = "ATTACKAT1200AM"
    trans_key = "PRIVACY"
    assert ciphers.adfgvx.encrypt(plaintext, trans_key, alpha_6x6) == "DGDDDAGDDGAFADDFDADVDVFAADVX"


def test_decrypt_6x6():
    ciphertext = "DGDDDAGDDGAFADDFDADVDVFAADVX"
    trans_key = "PRIVACY"
    assert ciphers.adfgvx.decrypt(ciphertext, trans_key, alpha_6x6) == "ATTACKAT1200AM"


def test_bad_alpha_square():
    alpha_5x5 = [
        ["b", "b", "a", "l", "p"],
        ["d", "h", "o", "z", "k"],
        ["q", "f", "v", "s", "n"],
        ["g", "i", "c", "u", "x"],
        ["m", "r", "e", "w", "y"]
    ]
    plaintext = "ATTACKATONCE"
    trans_key = "CARGO"

    try:
        ciphers.adfgvx.encrypt(plaintext, trans_key, alpha_5x5) == "FAXDFADDDGDGFFFAFAXAFAFX"
        assert False
    except ValueError:
        assert True


def test_load_alpha_square5x5():
    expected = alpha_5x5
    actual = ciphers.adfgvx.load_alpha_square(open("tests/adfgvx_square5x5", "r"))
    assert actual == expected


def test_load_alpha_square6x6():
    expected = alpha_6x6
    actual = ciphers.adfgvx.load_alpha_square(open("tests/adfgvx_square6x6", "r"))
    assert actual == expected


def test_load_alpha_square_bad_shape():
    try:
        ciphers.adfgvx.load_alpha_square(open("tests/adfgvx_square6x6_bad_shape", "r"))
        assert False
    except ValueError:
        assert True