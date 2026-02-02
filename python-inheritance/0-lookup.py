#!/usr/bin/python3
"""
This module provides a function to retrieve the list of available
attributes and methods of an object.
"""


def lookup(obj):
    """
    lookup - Returns the list of available attributes and methods of an object

    @obj: The object to inspect

    Return: A list containing the names of the object's attributes and methods
    """
    list = dir(obj)
    return list
