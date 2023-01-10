#!/usr/bin/python3
"""
This module contains a function that works with json
"""
import json


def save_to_json_file(my_obj, filename):
    """
    This function saves objs to json file
    """
    with open(filename, 'w+', encoding='utf8') as f:
        f.write(json.dumps(my_obj))
