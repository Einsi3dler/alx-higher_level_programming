#!/usr/bin/python3
"""
This module has a single function that print a square
"""


def print_square(size):
    """
    This function accepts a value(int) and print:
    """
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) == float and size < 0:
        raise TypeError("size must be an integer")
    for x in range(size):
        for x in range(size):
            print("#", end="")
        print()
