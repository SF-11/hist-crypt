from ciphers import caesar
import re


def import_dict(file):
    """imports a mapping of characters in the specified filename

    Args:
        filename (str): name of file containing mapping of letters:
                        A\tZ
                        B\tY
                        C\tX

    Returns:
        {char -> char}: mappings to swap characters
    """
    mappings = {}
    line_format = re.compile(r".\t.")

    for line in file:
        if not line_format.match(line):
            # skip invalid line formats
            continue

        line = line.rstrip()
        pair = line.split("\t")
 
        if pair[0] in mappings or pair[1] in mappings:
            # skip duplicate entries
            continue

        mappings[pair[0]] = pair[1]
        mappings[pair[1]] = pair[0] 

    return mappings


def export_dict(mapping, filename):
    """Export mapping of swap characters to a file

    Args:
        mapping ({char -> char}): mapping of swapped characters like:
                                  A\tZ
                                  B\tY
                                  C\tX

        filename (str): file to save mapping in

    Returns:
        File: file object containing mappings
    """
    f = open(filename, "w")

    # remove duplicates
    mapping_deduplicate = {}
    for key in mapping.keys():
        if key in mapping_deduplicate.keys() or key in mapping_deduplicate.values():
            continue
        else:
            mapping_deduplicate[key] = mapping[key]

    keys = sorted(mapping_deduplicate.keys())
    for key in range(len(keys)):
        f.write(keys[key] + "\t" + mapping[keys[key]])
        if not key == len(keys) - 1:
            f.write("\n")

    f.close()

    return f


def substitute(text, mapping, case_sensitive=False):
    """Swap characters in text as specified in the mapping

    Args:
        text (str): initial un-substituted text 
        mapping ({char -> char}): mapping of swapped characters like:
                                  A\tZ
                                  B\tY
                                  C\tX

        case_sensitive (bool, optional): set text to upper if false
                                         defaults to false

    Returns:
        str: text after letter substitutions have been made
    """
    if not case_sensitive:
        text = text.upper()

    new_text = ""
    
    for letter in text:
        if letter in mapping:
            new_text += mapping[letter]
        else:
            new_text += letter

    return new_text


def crack(text):
    """predect letter mappings using frequency analysis
       FIXME delete prints, return string

    Args:
        text (str): encrypted text
    """
    freqs = caesar.freq(text)
    eng_freqs = caesar.english_letter_frequency()

    sorted_freqs = sorted(freqs.keys(), key=lambda k: freqs[k], reverse=True)
    sorted_eng = sorted(eng_freqs.keys(), key=lambda k: eng_freqs[k], reverse=True)

    print(sorted_freqs)
    for i in range(26):
        print(sorted_freqs[i], format(freqs[sorted_freqs[i]], ".03f"))

    print()
    print(sorted_eng)
    for i in range(26):
        print(sorted_eng[i], format(eng_freqs[sorted_eng[i]], ".03f"))

    new_text = ""

    for letter in text:
        if letter.isalpha():
            idx = sorted_freqs.index(letter)
            new_text += sorted_eng[idx]

        else:
            new_text += letter

    print(new_text)
