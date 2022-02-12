import random


LOOKUP = {
    "A": "aaaaa", "aaaaa": "A",
    "B": "aaaab", "aaaab": "B",
    "C": "aaaba", "aaaba": "C",
    "D": "aaabb", "aaabb": "D",
    "E": "aabaa", "aabaa": "E",
    "F": "aabab", "aabab": "F",
    "G": "aabba", "aabba": "G",
    "H": "aabbb", "aabbb": "H",
    "I": "abaaa", "J": "abaaa", "abaaa": "I",
    "K": "abaab", "abaab": "K",
    "L": "ababa", "ababa": "L",
    "M": "ababb", "ababb": "M",
    "N": "abbaa", "abbaa": "N",
    "O": "abbab", "abbab": "O",
    "P": "abbba", "abbba": "P",
    "Q": "abbbb", "abbbb": "Q",
    "R": "baaaa", "baaaa": "R",
    "S": "baaab", "baaab": "S",
    "T": "baaba", "baaba": "T",
    "U": "baabb", "V": "baabb", "baabb": "V",
    "W": "babaa", "babaa": "W",
    "X": "babab", "babab": "X",
    "Y": "babba", "babba": "Y",
    "Z": "babbb", "babbb": "Z"
}

LOOKUP_UNIQUE = {
    "A": "aaaaa", "aaaaa": "A",
    "B": "aaaab", "aaaab": "B",
    "C": "aaaba", "aaaba": "C",
    "D": "aaabb", "aaabb": "D",
    "E": "aabaa", "aabaa": "E",
    "F": "aabab", "aabab": "F",
    "G": "aabba", "aabba": "G",
    "H": "aabbb", "aabbb": "H",
    "I": "abaaa", "abaaa": "I",
    "J": "abaab", "abaab": "I",
    "K": "ababa", "ababa": "K",
    "L": "ababb", "ababb": "L",
    "M": "abbaa", "abbaa": "M",
    "N": "abbab", "abbab": "N",
    "O": "abbba", "abbba": "O",
    "P": "abbbb", "abbbb": "P",
    "Q": "baaaa", "baaaa": "Q",
    "R": "baaab", "baaab": "R",
    "S": "baaba", "baaba": "S",
    "T": "baabb", "baabb": "T",
    "U": "babaa", "babaa": "U", 
    "V": "babab", "babab": "V",
    "W": "babba", "babba": "W",
    "X": "babbb", "babbb": "X",
    "Y": "bbaaa", "bbaaa": "Y",
    "Z": "bbaab", "bbaab": "Z"
}


def encrypt(message, text="", unique=False):
    """not really encrypting... more like encoding"""
    if text != "" and len(text) < 5 * len(message):
        raise ValueError("Text must be at least 5 times the length of the message to hide")

    lookup_dict = LOOKUP_UNIQUE if unique else LOOKUP

    # encode all of the letters in a's and b's
    message = message.upper()
    ab = ""
    for letter in message:
        if letter.isalpha():
            ab += lookup_dict[letter]

    # have the option to just encode and not hide in text
    if text == "":
        return ab 

    # hide the message in the text
    hidden = ""
    text = text.lower()
    ab_idx = 0
    text_idx = 0
    while ab_idx < len(ab):
        if text[text_idx].isalpha():
            hidden += text[text_idx] if ab[ab_idx] == "a" else text[text_idx].upper()
            ab_idx += 1
        else:
            hidden += text[text_idx]
        text_idx += 1

    # randomize the capitalization of the rest of the text
    for i in range(text_idx, len(text)):
        rand = random.randint(0, 1)
        hidden += text[i] if rand == 0 else text[i].upper()

    return hidden


def decrypt(text, unique=False):
    """not really decrypting... more like decoding"""

    lookup_dict = LOOKUP_UNIQUE if unique else LOOKUP

    ab = ""
    for letter in text:
        if letter.isalpha():
            ab += "b" if letter.isupper() else "a"

    msg = ""
    for i in range(len(ab) // 5):
        try:
            msg += lookup_dict[ab[i*5:(i*5)+5]]
        except LookupError:
            break

    return msg

    
if __name__ == "__main__":
    print(encrypt("steganography", "To encode a message each letter of the plaintext is replaced by a group of five of the letters 'A' or 'B'."))
    print(decrypt("To enCOde A mesSage eACh letter OF the PLaIntEXt Is replaced bY A GrouP OF FiVE of tHE LetTERs 'a' OR 'B'."))

    