#!/usr/bin/python3
"""
This module provides a function to print a text with proper indentation.

The text is printed with two new lines after each occurrence of the
characters '.', '?' and ':'.
"""


def text_indentation(text):
    """
    text_indentation - Prints a text with 2 new lines after '.', '?' and ':'.

    Description:
        Iterates through the given text and prints it line by line.
        Each time one of the characters '.', '?' or ':' is encountered,
        the current line is printed (without leading/trailing spaces)
        followed by two newline characters.

    Args:
        text (str): The text to be formatted and printed.

    Raises:
        TypeError: If text is not a string.

    Returns:
        None
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    line = ""
    for c in text:
        if c in ".?:":
            line += c
            print(line.strip())
            print()
            line = ""
        else:
            line += c
    if line.strip():
        print(line.strip(), end="")
           
