#!/usr/bin/env python3
"""Module demonstrating the use of mixins to compose
swimming and flying behaviors."""


class SwimMixin():
    """Mixin providing swimming behavior to a class."""
    def swim(self):
        """Print a message indicating the creature is swimming."""
        print("The creature swims!")


class FlyMixin ():
    """Mixin providing flying behavior to a class."""
    def fly(self):
        """Print a message indicating the creature is flying."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Class representing a dragon that can swim and fly using mixins."""
    def roar(self):
        """Print a message indicating the dragon is roaring."""
        print("The dragon roars!")
