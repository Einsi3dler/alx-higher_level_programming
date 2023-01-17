#!/usr/bin/python3
"""
This module contains an empty class
"""


import json
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

    def to_json_string(list_dictionaries):
        """
        """
        res = []
        if list_dictionaries is None:
            return res
        return (json.dumps(list_dictionaries))
