#!/usr/bin/python3
"""
This module defines a custom list class
"""


class MyList(list):
    """
    This class inherits from list and adds a method to print the list sorted.
    """

    def print_sorted(self):
        """
        print_sorted - Prints the list elements in ascending sorted order
        """

        print(sorted(self))
