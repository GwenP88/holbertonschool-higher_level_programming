#!/usr/bin/python3
"""
This module defines a Square class that inherits from Rectangle.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square - Square class that inherits from Rectangle
    """

    def __init__(self, size):
        """
        __init__ - Initializes a Square

        @size: Size of the square

        Return: None
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        area - Returns the area of the rectangle

        Return: Rectangle area
        """
        return self.__size * self.__size
