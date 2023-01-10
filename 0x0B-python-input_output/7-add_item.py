#!/usr/bin/python3
"""
This module contains a function that interacts with Json
"""
import sys
import json
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

f_nm = "add_item.json"
flag = 0
try:
    data = load_from_json_file(f_nm)
    for val in sys.argv:
        flag += 1
        if flag != 1:
            data.append(val)
    save_to_json_file(data, f_nm)
except Exception:
    save_to_json_file(sys.argv[1:], f_nm)
