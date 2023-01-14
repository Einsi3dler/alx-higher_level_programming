#!/usr/bin/python3
"""
This module contains an empty class
"""


class Base:
    """
    This class contains a struture with IDs
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        intialization
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
