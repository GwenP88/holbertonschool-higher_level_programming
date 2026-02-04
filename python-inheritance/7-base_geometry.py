#!/usr/bin/python3
"""
This module defines BaseGeometry.
"""


class BaseGeometry:
    """
    BaseGeometry - Base geometry class
    """

    def area(self):
        """
        area - Raises an exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates an integer value

        @name (str): Name of the parameter
        @value (int): Value to validate
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
