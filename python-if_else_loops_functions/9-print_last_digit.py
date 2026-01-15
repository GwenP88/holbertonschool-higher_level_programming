#!/usr/bin/python3
def print_last_digit(number):
    n = number
    if n < 0:
        n = - n
    last_digit = n % 10
    print("{}".format(last_digit), end="")
    return last_digit
