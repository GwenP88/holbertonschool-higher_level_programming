#!/usr/bin/python3
"""
This module defines MyInt.
"""


class MyInt (int):
    """
    MyInt - Rebel integer class that inverts == and !=
    """

    def __eq__(self, other):
        """
        __eq__ - Inverts equality comparison

        @other: Value to compare with

        Return: True or False
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        __ne__ - Inverts inequality comparison

        @other: Value to compare with

        Return: True or False
        """
        return super().__eq__(other)
