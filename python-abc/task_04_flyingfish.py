#!/usr/bin/env python3
"""Module demonstrating multiple inheritance with
Fish, Bird, and FlyingFish classes."""


class Fish():
    """Class representing a fish with swimming behavior and a water habitat."""

    def swim(self):
        """Print a message indicating the fish is swimming."""
        print("The fish is swimming")

    def habitat(self):
        """Print a message indicating the fish habitat."""
        print("The fish lives in water")


class Bird():
    """Class representing a bird with flying behavior and a sky habitat."""

    def fly(self):
        """Print a message indicating the bird is flying."""
        print("The bird is flying")

    def habitat(self):
        """Print a message indicating the bird habitat."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """Class representing a flying fish inheriting from both Fish and Bird."""

    def fly(self):
        """Print a message indicating the flying fish is flying."""
        print("The flying fish is soaring!")

    def swim(self):
        """Print a message indicating the flying fish is swimming."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Print a message indicating the flying fish habitat."""
        print("The flying fish lives both in water and the sky!")
