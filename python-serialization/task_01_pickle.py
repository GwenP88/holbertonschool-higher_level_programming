#!/usr/bin/env python3
"""Serialize and deserialize a custom object using pickle"""
import pickle


class CustomObject:
    """Represent a simple object that can be pickled to/from a file."""

    def __init__(self, name, age, is_student=True):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Print the object attributes."""
        print("Name: {}\nAge: {}\nIs Student: {}".format(
            self.name, self.age, self.is_student))

    def serialize(self, filename):
        """Save the current instance to a file using pickle"""
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except (OSError, pickle.PicklingError, TypeError):
            return None

    @classmethod
    def deserialize(cls, filename):
        """Load and return an instance from a pickle file"""
        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
        except (FileNotFoundError, pickle.UnpicklingError, OSError, EOFError):
            return None
