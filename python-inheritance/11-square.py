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
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


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

    def __str__(self):
        """
        __str__ - Returns the string representation of the square

        Return: String representation
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
