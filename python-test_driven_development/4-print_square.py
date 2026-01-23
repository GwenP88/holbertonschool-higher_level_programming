#!/usr/bin/python3
"""
This module provides a function that prints a square using the '#' character.

The square size is defined by an integer parameter. The function validates
the type and value of the parameter and raises appropriate exceptions when
the input is invalid.
"""


def print_square(size):
    """
    print_square prints a square with the character '#'.

    The size of the square is defined by the parameter size.
    The function prints
    size lines, each containing size '#' characters.

    Args:
        size (int): The length of each side of the square.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.

    Return:
        None
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    square = "#" * size
    for i in range(size):
        print("{}".format(square))
