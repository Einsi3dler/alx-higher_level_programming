#!/usr/bin/python3
"""
This modules contains a single class
"""


class Square:
    """
    This class contains two function
    """
    def __init__(self, size=0):
        """
        this initializes the square and validates the value
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        this is meant to calculate the general area of a square
        """
        val = self.__size
        return val * val
