#!/usr/bin/python3
"""
This module contains a function that interacts with Json
"""
import sys
import json
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

res = []
for num in range(1, len(sys.argv)):
    res.append(sys.argv[val])

with open ("add_item.json", 'w+', enconding='utf8'):
    load_from_json_file()
