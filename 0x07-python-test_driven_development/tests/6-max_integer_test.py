#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    Test case class
    """
    def test_value(self):
        """
        Function for tests case
        """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([4, 2, 3, 1]), 4)
        self.assertEqual(max_integer([1, 2, 5, 4, 3]), 5)
        self.assertEqual(max_integer([4, 2, -3, 1]), 4)
        self.assertEqual(max_integer([-4, -2, -3, -1]), -1)
        self.assertEqual(max_integer([4]), 4)
        self.assertIsNone(max_integer([]), "Test value is not none")


if __name__ == '__main__':
    unittest.main()
