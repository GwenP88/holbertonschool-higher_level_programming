#!/usr/bin/python3
"""
This module provides a simple arithmetic helper function.
It defines add_integer() to add two numbers after validating their types.
"""


def add_integer(a, b=98):
    """
    Add two numbers after validating their types.

    Args:
        a: The first number to add (integer or float).
        b: The second number to add (integer or float), defaults to 98.

    Returns:
        The integer result of adding a and b.

    Raises:
        TypeError: If a or b is not an integer or a float.
    """

    if not (type(a) is int or type(a) is float):
        raise TypeError("a must be an integer")
    if not (type(b) is int or type(b) is float):
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return (a + b)
