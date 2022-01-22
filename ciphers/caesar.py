"""
TODO
filename: caesar.py

decrypts and encrypts texts using a Caesar shift cipher

TODO extract util functionality (shift)
"""
import re  # regex pattern matching user input
import argparse


def eval_ciphertext(ciphertext):
    """
    This is the primary function for the general evaluation of a ciphertext. This includes:
     - finding the frequency of each letter in the ciphertext
     - finding recommended shift keys
     - printing the ciphertext after shifting it with the most recommended key
     - printing other recommendations if the best key was wrong

    :param ciphertext: the encoded string
    """
    ciphertext = ciphertext.upper()
    text_freq = freq(ciphertext)
    return get_shift_keys(ciphertext, text_freq)


def freq(ciphertext):
    """
    Iterates through a ciphertext and totals the occurrences of each letter

    :param ciphertext: the encoded string
    :return: a dictionary mapping English letters to their frequency in the given text
    """
    freq_dict = empty_freq_dict()
    total = 0

    # total up the frequency
    for letter in ciphertext:
        if letter.isalpha():
            freq_dict[letter] += 1
            total += 1

    # calculate percentage of use
    for letter in freq_dict:
        if freq_dict[letter] != 0:
            freq_dict[letter] = freq_dict[letter] / total * 100

    return freq_dict


def get_shift_keys(ciphertext, text_freq):
    """
    FIXME if the text has fewer than three different characters it can cause problems

    For each letter in the ciphertext, its 'closest letter' is found.  The difference between the closest
    letter and the original represents a shift key. Occurrences of shift keys are totaled, at the top 3
    are returned.

    :param ciphertext: the encoded string
    :param text_freq: a dictionary mapping the frequency of each letter in the text
    :return: a 3-tuple of ints containing the top 3 options for shift keys
    """
    # find out the most common shift using letter frequency
    shift_freq = {}

    for letter in ciphertext:
        if letter.isalpha():
            # get a similar letter from standard letter frequency
            cleartext_letter = closest_letter(text_freq[letter])
            shift_num = ord(cleartext_letter) - ord(letter)

            if shift_num not in shift_freq:
                shift_freq[shift_num] = 0

            shift_freq[shift_num] += 1

    shift_keys = sorted(shift_freq.keys(), key=lambda k: shift_freq[k], reverse=True)
    shift_keys += [0] * (3 - len(shift_keys))  # FIXME temp solution for fewer than 3 chars
    return shift_keys[0], shift_keys[1], shift_keys[2]


def shift(ciphertext, shift_key):
    """
    Performs a rot shift on a text

    :param ciphertext: the encoded string
    :param shift_key: the amount you want to shift by
    :return: a string representing the ciphertext after it has been shifted
    """
    if not isinstance(shift_key, int):
        raise ValueError()

    ciphertext = ciphertext.upper()
    cleartext = ""

    for letter in ciphertext:
        if letter.isalpha():
            new_letter = chr((((ord(letter) - 65) + shift_key) % 26) + 65)
            cleartext += new_letter

        else:
            # just copies all whitespace and other symbols
            cleartext += letter

    return cleartext


def closest_letter(freq_percentage):
    """
    Finds the 'closest letter' by comparing the percentage of use in a given text
    to the standard English frequency percentages

    :param freq_percentage: frequency percentage of a certain letter in a ciphertext
    :return: the letter that the percentage most closely corresponds to
    """
    standard_freq = english_letter_frequency()

    closest_val = min(standard_freq.values(), key=lambda val: abs(float(val) - freq_percentage))

    for letter in standard_freq:
        if standard_freq[letter] == closest_val:
            return letter


def empty_freq_dict():
    """
    :return: a dictionary mapping English letters to their frequency in a text, initialized to 0
    """
    return {
        "A": 0,
        "B": 0,
        "C": 0,
        "D": 0,
        "E": 0,
        "F": 0,
        "G": 0,
        "H": 0,
        "I": 0,
        "J": 0,
        "K": 0,
        "L": 0,
        "M": 0,
        "N": 0,
        "O": 0,
        "P": 0,
        "Q": 0,
        "R": 0,
        "S": 0,
        "T": 0,
        "U": 0,
        "V": 0,
        "W": 0,
        "X": 0,
        "Y": 0,
        "Z": 0,
    }


def english_letter_frequency():
    """
    Figures taken from the Wikipedia article on Letter Frequency

    :return: dictionary mapping English letters to their frequency, given in percentages
    """
    return {
        "E": 12.70,
        "T": 9.056,
        "A": 8.167,
        "O": 7.507,
        "I": 6.966,
        "N": 6.749,
        "S": 6.327,
        "H": 6.094,
        "R": 5.987,
        "D": 4.253,
        "L": 4.025,
        "C": 2.782,
        "U": 2.758,
        "M": 2.406,
        "W": 2.360,
        "F": 2.228,
        "G": 2.015,
        "Y": 1.974,
        "P": 1.929,
        "B": 1.492,
        "V": .978,
        "K": .772,
        "J": .153,
        "X": .150,
        "Q": .095,
        "Z": .074
    }


def main():
    parser = argparse.ArgumentParser(description="Encrypts/Decrypts shift ciphers")
    parser.add_argument("-f", "--file")
    args = parser.parse_args()

    orig_text = ""

    try:
        fd = open(args.file, "r")
        orig_text = fd.read().upper().strip()

    except TypeError:
        pass  # FIXME

    except FileNotFoundError:
        pass  # FIXME

    curr_text = orig_text

    # set regex patterns for program loop
    # FIXME add help message
    shift_pattern = re.compile(r"shift\s+(-?\d+)")
    new_pattern = re.compile(r"new\s+\"(.+)\"")
    reset_pattern = re.compile("reset")
    eval_pattern = re.compile("eval")

    # main program loop
    while True:

        print("ORIGINAL TEXT:")
        print(orig_text)
        print()

        print("CURRENT TEXT:")
        print(curr_text)
        print()

        cmd = input("> ")

        if cmd.lower() == "q" or cmd.lower() == "quit":
            break

        elif shift_pattern.match(cmd):
            match = shift_pattern.match(cmd)
            shift_key = match.group(1)
            curr_text = shift(curr_text.upper(), int(shift_key))

        elif new_pattern.match(cmd.lower()):
            match = new_pattern.match(cmd.lower())
            orig_text = match.group(1)
            curr_text = orig_text

        elif eval_pattern.match(cmd):
            shift_keys = eval_ciphertext(curr_text)
            print("Recommended shift keys: ", shift_keys)

        elif reset_pattern.match(cmd):
            curr_text = orig_text

        else:
            print("SHIFTER DECODER\n")
            print("An interactive console to shift around a text\n")
            print("Usage:")
            print(" python3 caesar.py [text file]\n")  # FIXME
            print("Commands:")
            print(" q[uit]          quits the program")
            print(" new <text>      sets a new 'original text'")
            print(" shift <num>     shifts the text <num> places")
            print(" reset           resets your working text to the original text")
            print(" eval            Recommends 3 shift keys to try based on freq. analysis")

        print()


if __name__ == "__main__":
    main()
