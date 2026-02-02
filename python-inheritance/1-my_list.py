#!/usr/bin/python3
"""
This module defines a custom list class that can print its elements in
sorted order.
"""


class MyList (list):
    """
    MyList - Defines a custom list object.

    This class inherits from list and adds a method to print the list sorted.
    """

    def print_sorted(self):
        """
        print_sorted - Prints the list elements in ascending sorted order

        Return: None
        """

        print(sorted(self))
