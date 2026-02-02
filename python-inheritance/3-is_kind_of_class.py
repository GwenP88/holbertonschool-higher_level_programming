#!/usr/bin/python3
"""
This module provides is_kind_of_class.
"""


def is_kind_of_class(obj, a_class):
    """
    is_kind_of_class - Checks if obj is an instance of a_class or a subclass

    @obj: Object to check
    @a_class: Reference class

    Return: True or False
    """
    return isinstance(obj, a_class)
