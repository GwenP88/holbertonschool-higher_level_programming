#!/usr/bin/python3
"""
This module provides inherits_from.
"""


def inherits_from(obj, a_class):
    """
    inherits_from - Checks if obj inherits from a_class

    @obj: Object to check
    @a_class: Reference class

    Return: True or False
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
