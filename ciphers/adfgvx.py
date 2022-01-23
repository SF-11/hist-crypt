

adfgx = ["A", "D", "F", "G", "X"]
adfgvx = ["A", "D", "F", "G", "V", "X"]


def _find_letter(letter, alphabet_square):
    for i in range(len(alphabet_square)):
        for j in range(len(alphabet_square)):
            if letter.upper() == alphabet_square[i][j].upper():
                return i, j

    return -1, -1


def encrypt(text, key, alphabet_square):
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
    sorted_key = "".join(sorted(key))

    # init columns dictionary
    col_dict = {}
    for letter in key:
        col_dict[letter] = []

    # find out how many letters per col
    letters_per_col = {}
    for letter in key:
        letters_per_col[letter] = 0
    key_idx = 0
    for _ in ciphertext:
        letters_per_col[key[key_idx]] += 1
        key_idx = (key_idx + 1) % len(key)

    # sort letters into columns
    i = 0
    sorted_key_idx = 0
    for letter in ciphertext:
        col_dict[sorted_key[sorted_key_idx]] += letter
        i = (i + 1)
        if i == letters_per_col[sorted_key[sorted_key_idx]]:
            i = 0
            sorted_key_idx += 1

    #
    ordered_text = ""
    for i in range(len(col_dict[sorted_key[0]])):
        for j in sorted_key:
            if len(col_dict[j]) == len(col_dict[sorted_key[0]]):
                ordered_text += col_dict[j][i]

    #
    idx_list = []
    for val in ordered_text:
        if len(alphabet_square) == 5:
            idx_list += [adfgx.index(val)]
        else:
            idx_list += [adfgvx.index(val)]

    #
    plaintext = ""
    for i in range(0, len(idx_list)-2, 2):
        plaintext += alphabet_square[idx_list[i]][idx_list[i+1]]

    return plaintext


if __name__ == "__main__":
    
    alpha_square = [
        ['b', 't', 'a', 'l', 'p'],
        ['d', 'h', 'o', 'z', 'k'],
        ['q', 'f', 'v', 's', 'n'],
        ['g', 'ij', 'c', 'u', 'x'],
        ['m', 'r', 'e', 'w', 'y']
    ]
    
    