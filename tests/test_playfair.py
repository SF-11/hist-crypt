import ciphers.playfair


def test_build_grid():
    expected = [['P', 'L', 'A', 'Y', 'F'],
                ['I', 'R', 'E', 'X', 'M'],
                ['B', 'C', 'D', 'G', 'H'],
                ['K', 'N', 'O', 'Q', 'S'],
                ['T', 'U', 'V', 'W', 'Z']]
    assert ciphers.playfair.build_grid("PLAYFAIREXAMPLE") == expected


def test_build_grid_long():
    expected = [['A', 'Z', 'B', 'C', 'D'],
                ['E', 'F', 'G', 'H', 'I'],
                ['K', 'L', 'M', 'N', 'O'],
                ['P', 'Q', 'R', 'S', 'T'],
                ['U', 'V', 'W', 'X', 'Y']]
    assert ciphers.playfair.build_grid("AAAAAAAAAAAAAAAAAAAAAAAAAAZ") == expected


def test_build_grid_i_j():
    expected = [['I', 'A', 'B', 'C', 'D'],
                ['E', 'F', 'G', 'H', 'K'],
                ['L', 'M', 'N', 'O', 'P'],
                ['Q', 'R', 'S', 'T', 'U'],
                ['V', 'W', 'X', 'Y', 'Z']]
    assert ciphers.playfair.build_grid("IJ") == expected


def test_build_grid_non_alpha():
    try:
        ciphers.playfair.build_grid("! ^ #")
        assert False
    except ValueError:
        assert True


def test_build_grid_lower():
    expected = [['Z', 'Y', 'X', 'A', 'B'],
                ['C', 'D', 'E', 'F', 'G'],
                ['H', 'I', 'K', 'L', 'M'], 
                ['N', 'O', 'P', 'Q', 'R'],
                ['S', 'T', 'U', 'V', 'W']]
    assert ciphers.playfair.build_grid("zyx") == expected


def test_encrypt():        
    assert ciphers.playfair.encrypt("HIDETHEGOLDINTHETREESTUMP", "PLAYFAIREXAMPLE") == "BMODZBXDNABEKUDMUIXMMOUVIF"


def test_encrypt_non_alpha():
    assert ciphers.playfair.encrypt("HIDE THE GOLD IN THE TREE STUMP", "PLAYFAIREXAMPLE") == "BMODZBXDNABEKUDMUIXMMOUVIF"



def test_encrypt_odd():
    assert ciphers.playfair.encrypt("HIDETHEGOLDINTHETREESTUM", "PLAYFAIREXAMPLE") == "BMODZBXDNABEKUDMUIXMMOUVIM"


def test_encrypt_i_j():
    assert ciphers.playfair.encrypt("IJ", "PLAYFAIREXMAPLE") == "RMRM"


def test_encrypt_lower():
    assert ciphers.playfair.encrypt("hidethegoldinthetreestump", "PLAYFAIREXAMPLE") == "BMODZBXDNABEKUDMUIXMMOUVIF"


def test_decrypt():
    assert ciphers.playfair.decrypt("BMODZBXDNABEKUDMUIXMMOUVIF", "PLAYFAIREXAMPLE") == "HIDETHEGOLDINTHETREXESTUMP"


def test_decrypt_non_alpha():
    assert ciphers.playfair.decrypt("! ^ %", "PLAYFAIREXAMPLE") == ""
      

def test_decrypt_odd():
    ciphers.playfair.decrypt("BMODZBXDNABEKUDMUIXMMOUVI", "PLAYFAIREXAMPLE") == "HIDETHEGOLDINTHETREXESTUME"



def test_decrypt_i_j():
    assert ciphers.playfair.decrypt("IJ", "PLAYFAIREXMAPLE") == "MM"


def test_decrypt_lower():
    assert ciphers.playfair.decrypt("bmodzbxdnabekudmuixmmouvif", "PLAYFAIREXAMPLE") == "HIDETHEGOLDINTHETREXESTUMP"

