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

        Return: None
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        integer_validator - Validates an integer value

        @name: Name of the parameter
        @value: Value to validate

        Return: None
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
