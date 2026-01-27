#!/usr/bin/python3
"""
Square module.
"""


class Square:
    """
    Represents a square with validated size/position and printing support.
    """

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    def area(self):
        return self.size * self.size

    def __str__(self):
        string = ""
        if self.size == 0:
            return ""
        for i in range(self.position[1]):
            string += "\n"
        for j in range(self.size):
            string += " " * self.position[0] + "#" * self.size + "\n"
        string = string[:-1]
        return string

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integer")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integer")
        for x in value:
            if not isinstance(x, int) or x < 0:
                raise TypeError(
                    "position must be a tuple of 2 positive integer"
                )
        self.__position = value
