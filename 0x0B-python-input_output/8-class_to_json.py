#!/us/bin/python3
"""
This module contains a single func
"""


import json
def class_to_json(obj):
    """
    This func runs a detailed view of the class
    """
    return json.dumps(obj.__dict__)

