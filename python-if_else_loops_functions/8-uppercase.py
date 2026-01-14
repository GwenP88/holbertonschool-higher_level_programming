#!/usr/bin/python3
def uppercase(str):
    """
    prints a string in uppercase followed by a new line

    Params:
        str (str): a string
    Print:
        the string in uppercase
    """
    for c in str:
        new_c = c
        code = ord(c)
        if code >= 97 and code <= 122:
            new_code = code - 32
            new_c = chr(new_code)
        print("{}".format(new_c), end="")
    print()
