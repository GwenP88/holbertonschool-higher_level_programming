#!/usr/bin/python3
"""Define a Student class with
a JSON-serializable dictionary representation."""


class Student:
    """
    Student representation with public attributes and JSON export.
    """

    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieve a dictionary representation of the Student instance."""
        return self.__dict__
