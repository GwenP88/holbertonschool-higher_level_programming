#!/usr/bin/env python3
"""Define abstract shapes and print
their area and perimeter using duck typing.
"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class for shapes."""
    @abstractmethod
    def area(self):
        """Return the shape area."""
        pass

    @abstractmethod
    def perimeter(self):
        """Return the shape perimeter."""
        pass


class Circle(Shape):
    """Circle shape implementation."""
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Return the circle area."""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Return the circle perimeter."""
        return math.pi * 2 * self.radius


class Rectangle(Shape):
    """Rectangle shape implementation."""
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """Return the rectangle area."""
        return self.height * self.width

    def perimeter(self):
        """Return the rectangle perimeter."""
        return (self.height + self.width) * 2


def shape_info(shape):
    """Print the area and perimeter of a shape-like object."""
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
