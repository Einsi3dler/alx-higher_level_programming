#!/usr/bin/python3
"""
this contains a single function
"""


def is_same_class(obj, a_class):
    """
    this accepts two arguments an object and a class
    """
    if type(obj) == a_class:
        return True
    else:
        return False
