import re

adfgx = ["A", "D", "F", "G", "X"]
adfgvx = ["A", "D", "F", "G", "V", "X"]


def _find_letter(letter, alphabet_square):
    """helper function to find the  index of a specified letter in the 
       alphabet square

    Args:
        letter (char): letter to search for
        alphabet_square (list of list of str): adfgvx translation matrix

    Raises:
        ValueError: raised if letter is not in square

    Returns:
        (int, int): row, col indexes of the letter in the square
    """
    for i in range(len(alphabet_square)):
        for j in range(len(alphabet_square)):
            if letter.upper() == alphabet_square[i][j].upper():
                return i, j

    raise ValueError("Your alphabet square does not contain letter in plaintext:", letter)


def encrypt(text, key, alphabet_square):
    """encrypt the text using a key 5x5 or 6x6 ADFG(V)X square

    Args:
        text (str): plaintext to encrypt
        key (str): key for the column transposition
        alphabet_square (list of list of str): adfgvx translation matrix

    Returns:
        str: ciphertext
    """
    text = re.sub(r'\W+', '', text)
    
    # encode text to ADFGVX
    encoded = []
    for letter in text:
        i, j = _find_letter(letter, alphabet_square)
        
        if len(alphabet_square) == 5:
            encoded += adfgx[i]
            encoded += adfgx[j]
        else:
            encoded += adfgvx[i]
            encoded += adfgvx[j]

    # init columns dictionary
    col_trans = {}
    for letter in key:
        col_trans[letter] = []

    # populate columns before transposition
    trans_idx = 0
    for letter in encoded:
        col_trans[key[trans_idx]] += letter
        trans_idx = (trans_idx + 1) % len(key)

    # transpose columns
    sorted_key = "".join(sorted(key))
    ciphertext = ""
    for col in sorted_key:
        for letter in col_trans[col]:
            ciphertext += letter

    return ciphertext


def decrypt(ciphertext, key, alphabet_square):
    """decrypt the text using a key and a 5x5 or 6x6 ADFG(V)X square

    Args:
        ciphertext (str): ciphertext to decrypt
        key (str): key for the column transposition
        alphabet_square (list of list of str): adfgvx translation matrix

    Returns:
        str: plaintext
    """
    # filter all non-alpha-numeric characters and initialize
    ciphertext = re.sub(r'\W+', '', ciphertext)
    sorted_key = "".join(sorted(key))
    mat = [['']*len(key) for _ in range((len(ciphertext) // len(key)) + 1)]

    # re-construct the columns
    curr = 0
    for k in  sorted_key:
        idx = key.index(k)
        # TODO clean up
        if idx >= len(ciphertext) % len(key):
            for row in mat[:-1]:
                row[idx] = ciphertext[curr]
                curr += 1
        else:
            for row in mat:
                row[idx] = ciphertext[curr]
                curr += 1
    
    # build the unscrambled ciphertext string
    encoded = ""
    for row in mat:
        encoded += "".join(row)
    
    # re-construct plaintext
    idx_list = []
    for val in encoded:
        if len(alphabet_square) == 5:
            idx_list += [adfgx.index(val)]
        else:
            idx_list += [adfgvx.index(val)]
    
    plaintext = ""
    for i in range(0, len(idx_list)-1, 2):
        plaintext += alphabet_square[idx_list[i]][idx_list[i+1]]

    return plaintext.upper()


def load_alpha_square(alphafile):
    """loads the ADFG(V)X matrix from a file

    Args:
        alphafile (str): contents of the matrix file

    Raises:
        ValueError: raised if matrix is not square

    Returns:
        list of list of str: adfgvx translation matrix
    """
    alpha_square = []
    for line in alphafile:
        split_line = [i.strip() for i in line.split(',')]
        alpha_square.append(split_line)

    # make sure matrix is square
    if not all(len(i)==len(alpha_square) for i in alpha_square):
        raise ValueError("Input file is not 5x5 or 6x6")

    return alpha_square


    