#!/usr/bin/python3
"""
Square module.
"""


class Square:
    """
    Represents a square with a validated size, area, and print methods.
    """
    def __init__(self, size=0):
        self.size = size

    def area(self):
        return self.size * self.size

    def my_print(self):
        square = "#" * self.size
        if self.size == 0:
            print()
        for i in range(self.size):
            print("{}".format(square))

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
