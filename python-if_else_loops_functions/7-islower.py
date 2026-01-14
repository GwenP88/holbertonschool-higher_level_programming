#!/usr/bin/python3
def islower(c):
    """
    checks for lowercase character

    Params:
        c (str): a letter
    Returns:
        True if c is lowercase
        False otherwise
    """
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False
