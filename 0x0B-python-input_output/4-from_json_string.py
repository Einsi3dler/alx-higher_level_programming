#!/usr/bin/python3
"""
This module contains a single function
"""


import json
def from_jsoun_string(my_str):
    """
    function returns a python obj from a str
    """
    return json.loads(my_str)
