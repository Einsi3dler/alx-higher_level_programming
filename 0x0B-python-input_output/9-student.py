#!/usr/bin/python3
"""
This contains a single class
"""


class Student():
    """
    this class contains 3 pub atris and a func
    """
    def __init__(self, first_name, last_name, age):
        """
        Initialization of data
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        returns a json rep of file
        """
        return self.__dict__
