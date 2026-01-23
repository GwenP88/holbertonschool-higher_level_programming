#!/usr/bin/python3
"""Unittests for max_integer
"""
import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Tests for max_integer"""

    def test_empty_list(self):
        """Empty list should return None"""
        self.assertIsNone(max_integer([]))

    def test_one_element(self):
        """Single element list should return that element"""
        self.assertEqual(max_integer([7]), 7)

    def test_max_at_start(self):
        """Max is the first element"""
        self.assertEqual(max_integer([9, 7, 4, 1]), 9)

    def test_max_at_last(self):
        """Max is the last element"""
        self.assertEqual(max_integer([8, 7, 4, 9]), 9)

    def test_max_at_middle(self):
        """Max is in the middle of the list"""
        self.assertEqual(max_integer([7, 9, 4, 1]), 9)

    def test_all_negative_numbers(self):
        """All numbers are negative"""
        self.assertEqual(max_integer([-10, -3, -7]), -3)

    def test_all_elements_equal(self):
        """All elements in the list are the same"""
        self.assertEqual(max_integer([2, 2, 2]), 2)

    def test_max_repeated(self):
        """Maximum value appears more than once in the list"""
        self.assertEqual(max_integer([1, 3, 3, 2]), 3)

    def test_with_floats(self):
        """List contains floating point numbers"""
        self.assertEqual(max_integer([1.5, 2.7, 2.6]), 2.7)

    def test_with_strings(self):
        """List contains string elements"""
        self.assertEqual(max_integer(["a", "z", "b"]), "z")


if __name__ == "__main__":
    unittest.main()
