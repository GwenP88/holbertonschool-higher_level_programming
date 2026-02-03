#!/usr/bin/env python3
"""Module defining a counted iterator
that tracks the number of items iterated."""


class CountedIterator():
    """Iterator wrapper that counts yielded items"""
    def __init__(self, obj_it):
        """Initialize the internal iterator and counter"""
        self.obj_it = iter(obj_it)
        self.count = 0

    def get_count(self):
        """Return the number of items iterated so far"""
        return self.count

    def __iter__(self):
        """Return self as an iterator"""
        return self

    def __next__(self):
        """Return next item and increment the counter"""
        current = next(self.obj_it)
        self.count += 1
        return current
