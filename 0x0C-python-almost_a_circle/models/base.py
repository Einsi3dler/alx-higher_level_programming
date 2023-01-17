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

    @classmethod
    def save_to_file(cls, list_objs):
        """
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as f:
            if list_objs is None:
                f.write("[]")
            else:
                list_dict = [o.to_dictionary() for o in  list_objs]
                f.write(cls.to_json_string(list_dict))

    @classmethod
    def create(cls, **dictionary):
    
    @staticmethod
    def from_json_string(json_string):
        """
        """
        if json_string is None or json_string == "":
            return []
        else:
            return(json.loads(json_string))
