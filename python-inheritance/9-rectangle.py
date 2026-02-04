#!/usr/bin/python3
"""
This module defines a Rectangle class that inherits from BaseGeometry.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle - Rectangle class that inherits from BaseGeometry
    """

    def __init__(self, width, height):
        """
        __init__ - Initializes a Rectangle

        @width: Rectangle width
        @height: Rectangle height

        Return: None
        """

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        area - Returns the area of the rectangle

        Return: Rectangle area
        """
        return self.__width * self.__height

    def __str__(self):
        """
        __str__ - Returns the string representation of the rectangle

        Return: String representation
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
