#!/usr/bin/python3
"""
This module contains one function
"""


def inherits_from(obj, a_class):
    """
    function returns True if the object is an instance of, or if the object\
    is an instance of a class that inherited from,\
    the specified class ; otherwise False.
    """
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    else:
        return False
