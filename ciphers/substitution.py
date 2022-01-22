"""
TODO
"""

from ciphers import caesar
import re


def import_dict(filename):
    """
    TODO
    """
    mappings = {}
    fd = open(filename, "r")
    line_format = re.compile(r".\t.")

    for line in fd:
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
    """TODO
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
    """TODO
    """
    if not case_sensitive:
        text = text.upper()

    new_text = ""
    
    for letter in text:
        if letter in mapping:
            new_text += mapping[letter]
        else:
            new_text += letter

    print(new_text)
    return new_text


def crack(text):
    """
    TODO 
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


def main_loop():
    """TODO
    """
    # FIXME this sucks ass

    orig_text = ""
    curr_text = orig_text
    mappings = {}

    # set regex patterns for program loop
    new_pattern = re.compile(r"new\s+\"(.+)\"")
    import_pattern = re.compile(r"import\s+\"(.+)\"")
    sub_pattern = re.compile(r"sub\s+\"(.)\"\s+\"(.)\"")

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

        elif new_pattern.match(cmd.lower()):
            match = new_pattern.match(cmd.lower())
            orig_text = match.group(1)
            curr_text = orig_text

        elif import_pattern.match(cmd.lower()):
            match = import_pattern.match(cmd)
            mappings = import_dict(match.group(1))
            curr_text = substitute(curr_text, mappings)

        elif sub_pattern.match(cmd.lower()):
            match = sub_pattern.match(cmd)
            val1 = match.group(1)
            val2 = match.group(2)

            if val1 in mappings:
                mappings.pop(mappings[val1])
                mappings.pop(val1)

            if val2 in mappings:
                mappings.pop(mappings[val2])
                mappings.pop(val2)

            mappings[val1] = val2
            mappings[val2] = val1

            curr_text = substitute(curr_text.upper(), mappings)

            # FIXME should edit mappings, not working

        else:
            # TODO
            print("TODO docs\n")

        print()


if __name__ == "__main__":
    main_loop()

