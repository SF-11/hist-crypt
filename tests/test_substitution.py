import pytest
from ciphers import substitution


def mappings():
    return {
        "A" : "Z",
        "Z" : "A",
        "B" : "Y",
        "Y" : "B",
        "C" : "X",
        "X" : "C",
        "D" : "W",
        "W" : "D",
        "E" : "V",
        "V" : "E",
        "F" : "U",
        "U" : "F",
        "G" : "T",
        "T" : "G",
        "H" : "S",
        "S" : "H",
        "I" : "R",
        "R" : "I",
        "J" : "Q",
        "Q" : "J",
        "K" : "P",
        "P" : "K",
        "L" : "O",
        "O" : "L",
        "M" : "N",
        "N" : "M",      
    }


def mappings_non_alpha():
    return {
        "A" : "Z",
        "Z" : "A",
        "B" : "Y",
        "Y" : "B",
        "C" : "X",
        "X" : "C",
        "D" : "W",
        "W" : "D",
        "E" : "V",
        "V" : "E",
        "F" : "U",
        "U" : "F",
        "G" : "T",
        "T" : "G",
        "H" : "S",
        "S" : "H",
        "I" : "R",
        "R" : "I",
        "J" : "Q",
        "Q" : "J",
        "K" : "P",
        "P" : "K",
        "L" : "O",
        "O" : "L",
        "M" : "N",
        "N" : "M", 
        "!" : "?",
        "?" : "!", 
    }


def mappings_missing_values():
    return {
        "A" : "Z",
        "Z" : "A",
        "B" : "Y",
        "Y" : "B",
        "C" : "X",
        "X" : "C",
        "D" : "W",
        "W" : "D",
        "F" : "U",
        "U" : "F",
        "G" : "T",
        "T" : "G",
        "I" : "R",
        "R" : "I",
        "J" : "Q",
        "Q" : "J",
        "K" : "P",
        "P" : "K",
        "L" : "O",
        "O" : "L",
        "M" : "N",
        "N" : "M", 
    }


def mapping_case_sensitive():
    return {
        "A": "Z",
        "a": "e",
        "B": "Y",
        "b": "f",
        "C": "X",
        "c": "g"
    }


def test_substitute():
    text = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    assert substitution.substitute(text, mappings()) == "ZYXWVUTSRQPONMLKJIHGFEDCBA"


def test_non_alpha():
    text = "!ABCDEFGHIJKLMNOPQRSTUVWXYZ?"
    assert substitution.substitute(text, mappings_non_alpha()) == "?ZYXWVUTSRQPONMLKJIHGFEDCBA!"


def test_missing_values():
    text = "HE'S NOT FROM THIS EARTH! :("
    assert substitution.substitute(text, mappings_missing_values()) == "HE'S MLG UILN GHRS EZIGH! :("


def test_case_sensitive():
    text = "AaBbCc"
    assert substitution.substitute(text, mapping_case_sensitive(), case_sensitive=True) == "ZeYfXg"


def test_non_case_sensitive():
    text = "AaBbCc"
    assert substitution.substitute(text, mapping_case_sensitive()) == "ZZYYXX"


def test_read():
    expected_dict = {
        "A": "Z",
        "Z": "A",
        "B": "Y",
        "Y": "B",
        "C": "X",
        "X": "C",
    }
    
    assert substitution.import_dict("tests/substitution_dict_1.txt") == expected_dict


def test_read_duplicated():
    expected_dict = {
        "A": "Z",
        "Z": "A",
        "B": "Y",
        "Y": "B",
        "C": "X",
        "X": "C",
    }
    
    assert substitution.import_dict("tests/substitution_dict_2.txt") == expected_dict


def test_read_non_alpha():
    expected_dict = {
        "!": "?",
        "?": "!",
        "&": "+",
        "+": "&",
        "%": "*",
        "*": "%",
    }
    
    assert substitution.import_dict("tests/substitution_dict_3.txt") == expected_dict


def test_read_invald_format():
    expected_dict = {
        "B": "Y",
        "Y": "B",
        "C": "X",
        "X": "C",
    }
    
    assert substitution.import_dict("tests/substitution_dict_4.txt") == expected_dict


def test_read_spaces():
    expected_dict = {
        " ": "A",
        "A": " "
    }

    assert substitution.import_dict("tests/substitution_dict_5.txt") == expected_dict


def test_export():
    dict_1 = {
        "A": "Z",
        "Z": "A",
        "B": "Y",
        "Y": "B",
        "C": "X",
        "X": "C",
        "!": "?",
    }
    expected_out = open("tests/substitution_dict_6.txt").read()

    fd = substitution.export_dict(dict_1, "tests/substitute_export.txt")
    assert fd.name == "tests/substitute_export.txt"
    assert open(fd.name, "r").read() == expected_out





