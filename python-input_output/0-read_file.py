#!/usr/bin/python3
"""File reading utility."""


def read_file(filename=""):
    """Read a UTF-8 text file and print it."""
    with open(filename, 'r', encoding="utf-8") as fichier:
        print("{}".format(fichier.read()), end="")
