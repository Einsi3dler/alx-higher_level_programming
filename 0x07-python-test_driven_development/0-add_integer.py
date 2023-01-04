#!/usr/bin/python3
"""
This module contains one function(eye roll, get your functions up noob lol)
"""


def add_integer(a, b=98):
    """
    This functions adds two numbers lol
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
