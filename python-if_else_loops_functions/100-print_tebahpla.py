#!/usr/bin/python3
for alphabet in range(122, 96, -1):
    if alphabet % 2 == 0:
        print("{}".format(chr(alphabet)), end="")
    else:
        upper_alphabet = chr(alphabet).upper()
        print("{}".format(upper_alphabet), end="")
