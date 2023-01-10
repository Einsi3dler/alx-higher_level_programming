#!/usr/bin/python3
"""
This module contains one function that interacts with Json
"""
import json


def load_from_json_file(filename):
    """
    This interacts with JSON file by loading up the objs
    """
    with open(filename, encoding='utf8') as f:
        data = f.read()
        return json.loads(data)
