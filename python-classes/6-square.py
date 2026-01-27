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

    def my_print(self):
        square = "#" * self.size
        if self.size == 0:
            print()
            return
        else:
            for i in range(self.position[1]):
                print()
        for j in range(self.size):
            for k in range(self.position[0]):
                print(" ", end="")
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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        for x in value:
            if not isinstance(x, int) or x < 0:
                raise TypeError(
                    "position must be a tuple of 2 positive integers"
                )
        self.__position = value
