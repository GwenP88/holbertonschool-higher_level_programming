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
    if c >= 'a' and c <= 'z':
        return True
    else:
        return False
