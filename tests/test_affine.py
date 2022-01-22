from ciphers import affine


def test_encrypt():
    assert affine.encrypt("AFFINECIPHER", 5, 8) == "IHHWVCSWFRCP"


def test_decrypt():
    assert affine.decrypt("IHHWVCSWFRCP", 5, 8) == "AFFINECIPHER"


def test_spaces():
    assert affine.encrypt(" AFFINE CIPHER ", 5, 8) == " IHHWVC SWFRCP "
    assert affine.decrypt(" IHHWVC SWFRCP ", 5, 8) == " AFFINE CIPHER "


def test_non_alpha():
    assert affine.encrypt("_AFFINE!CIPHER?", 5, 8) == "_IHHWVC!SWFRCP?"
    assert affine.decrypt("_IHHWVC!SWFRCP?", 5, 8) == "_AFFINE!CIPHER?"
