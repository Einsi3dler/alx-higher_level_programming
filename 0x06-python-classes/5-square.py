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
        self.__size = size

    @property
    def size(self):
        """
        This is a getter method
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        This is a setter method
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        this is meant to calculate the general area of a square
        """
        val = self.__size
        return val * val

    def my_print(self):
        """
        This file prints a representation of a square with #
        """
        val = self.__size
        if val == 0:
            print()
            return
        for x in range(val):
            for y in range(val):
                print(f"#", end="")
            print()
