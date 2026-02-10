#!/usr/bin/python3
"""Append text to a UTF-8 file."""


def append_write(filename="", text=""):
    """Append text to a file and return the number of characters added."""
    with open(filename, 'a', encoding="utf-8") as fichier:
        return fichier.write(text)
