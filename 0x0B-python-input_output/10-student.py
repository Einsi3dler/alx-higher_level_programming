#!/usr/bin/python3
"""
This module contains a single class
"""


class Student():
    """
    This class represents a JSON storage structure
    """
    def __init__(self, first_name, last_name, age):
        """
        initialization function
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        This json func intializes the storage structure
        """
        if attrs is None:
            data = sorted(self.__dict__)
            res = {}
            for val in data:
                res[val] = self.__dict__[val]
            return res
        else:
            data = self.__dict__
            res = {}
            arr = sorted(attrs)
            for val in arr:
                if val in data.keys():
                    res[val] = data[val]
                else:
                    pass
            return res
