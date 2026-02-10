#!/usr/bin/python3
"""Write text to a UTF-8 file."""


def write_file(filename="", text=""):
    """Write text to a file and return the number of characters written."""
    with open(filename, 'w', encoding="utf-8") as fichier:
        return fichier.write(text)
