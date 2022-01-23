import re
import argparse


def eval_ciphertext(ciphertext):
    """Primary function for the general evaluation of a ciphertext. This includes:
        - finding the frequency of each letter in the ciphertext
        - finding recommended shift keys
        - printing the ciphertext after shifting it with the most recommended key
        - printing other recommendations if the best key was wrong

    Args:
        ciphertext (str): encrypted text to crack

    Returns:
        (int, int, int): (1st_choice_key, 2nd_choice_key, 3rd_choice_key)
    """
    ciphertext = ciphertext.upper()
    text_freq = freq(ciphertext)
    return get_shift_keys(ciphertext, text_freq)


def freq(ciphertext):
    """Iterates through a ciphertext and total the occurances of each letter

    Args:
        ciphertext (str): encrypted text to crack

    Returns:
        {char -> float}: each different char in the ciphertext and the
                         percentage of the text they take up
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
    """Use frequency analysis to determine the top 3 most likely keys used to

    Args:
        ciphertext (str): encrypted text to crack
        text_freq ({char -> float}): each different char in the ciphertext
                                     and the percentage of the text they take up

    Returns:
        (int, int, int): (1st_choice_key, 2nd_choice_key, 3rd_choice_key)
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
    """Shifts the characters in ciphertext by shift_key spaces
       ex. "ABC" shifted by 2 -> "CDE" 

    Args:
        ciphertext (str): string to shift
        shift_key (int): amount the shift the string by

    Raises:
        ValueError: TODO

    Returns:
        str : shifted text
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
    """Find the letter that most closely matches the percentage of use
       in the standard English letter frequencies

    Args:
        freq_percentage (float): percent of the text represented 
                                 by a given letter

    Returns:
        char: letter that most closely matches the freq_percentage
    """
    standard_freq = english_letter_frequency()

    closest_val = min(standard_freq.values(), key=lambda val: abs(float(val) - freq_percentage))

    for letter in standard_freq:
        if standard_freq[letter] == closest_val:
            return letter


def empty_freq_dict():
    """mapping of English letters to their frequency in a text initialized to 0"""
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
    """Mapping of English letters to their frequency %, from Wikipedia"""
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
