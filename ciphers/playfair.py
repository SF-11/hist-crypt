

def encrypt(text, key):
    """use the Playfair cipher to encrypt the text

    Args:
        text (str): plaintext to encrypt
        key (str): keyword to use to derive Playfair table

    Returns:
        str: ciphertext
    """
    key_grid = build_grid(key)
    dim = len(key_grid)

    ciphertext = ""
    i = 0
    while i <= len(text) - 1:
        # get 2 char pair
        tmp = text[i:i+2]
        
        # split up double letters
        if tmp[0] == tmp[1]:
            tmp = tmp[0] + "X"
            i -= 1

        r_1, c_1 = search_2d(key_grid, tmp[0])
        r_2, c_2 = search_2d(key_grid, tmp[1])

        # if same row
        if r_1 == r_2:
            ciphertext += key_grid[r_1][c_1 + 1 % dim]
            ciphertext += key_grid[r_2][c_2 + 1 % dim]

        # if same col
        elif c_1 == c_2:
            ciphertext += key_grid[r_1 + 1 % dim][c_1]
            ciphertext += key_grid[r_2 + 1 % dim][c_2]

        # if square
        else:
            ciphertext += key_grid[r_1][c_2]
            ciphertext += key_grid[r_2][c_1]

        i += 2

    return ciphertext


def decrypt(text, key):
    # TODO
    pass


def build_grid(key):
    """build the grid used by the cipher the encrypt/decrypt

    Args:
        key (str): keyword of length <= 25

    Returns:
        list of list of str: 5x5 playfair key grid
    """
    key = key.upper().replace("J", "I")
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ" # skipped J, I=J for the purposes of this
    key_stream = "".join([key, alphabet])

    dim = 5 # dimension of the grid
    key_grid = [[""]*dim for _ in range(dim)]
    grid_i = grid_j = 0
    used = set()

    for k in key_stream:
        if k not in used:
            used.add(k)
            key_grid[grid_i][grid_j] = k
            grid_j = (grid_j + 1) % dim
            
            if grid_j is 0: 
                grid_i += 1

            if grid_i is dim:
                break

    return key_grid


def search_2d(arr, target):
    """
    TODO same func as in adfgvx
    """
    for row in range(len(arr)):
        for col in range(len(arr)):
            if arr[row][col] == target:
                return row, col

    return -1, -1





if __name__ == "__main__":
    
    grid = build_grid("PLAYFAIREXAMPLE")

    for i in grid:
        print(i)

    print(encrypt("HIDETHEGOLDINTHETREESTUMP", "PLAYFAIREXAMPLE"))