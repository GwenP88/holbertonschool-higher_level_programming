#!/usr/bin/env python3
from task_01_duck_typing import Circle, Rectangle, shape_info

circle = Circle(radius=5)
rectangle = Rectangle(width=4, height=7)

shape_info(circle)
shape_info(rectangle)

# ----- Test duck typing (area / perimeter comme attributs) -----
class FakeShape:
    def __init__(self, area, perimeter):
        self.area = area
        self.perimeter = perimeter


fake = FakeShape(123, 456)
shape_info(fake)