#!/usr/bin/python3
"""
This contains a relatively empty class
"""


class BaseGeometry():
    """
    This is the relatively empty class
    """
    def area(self):
        """
        This raises an error
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        This validates data
        """
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
