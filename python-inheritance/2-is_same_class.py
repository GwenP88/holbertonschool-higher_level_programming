#!/usr/bin/python3
"""
This module provides a function to check if an object is exactly an
instance of a specified class.
"""


def is_same_class(obj, a_class):
    """
    is_same_class - Checks if an object is exactly an instance of a given class

    @obj: The object to check
    @a_class: The class to compare the object's type with

    Return: True if obj is exactly an instance of a_class, otherwise False
    """

    return type(obj) is a_class
