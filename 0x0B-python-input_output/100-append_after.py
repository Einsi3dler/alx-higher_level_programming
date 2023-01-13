#!/usr/bin/python3
"""
This module contains a single function
"""
def append_after(filename="", search_string="", new_string=""):
    """
    This searches a file for a str and place a new str undee
    """
    lines = []
    with open(filename, 'r') as f:
        contents = f.readlines()
        for index, line in enumerate(contents):
            if search_string in line:
                lines.append(index)
    flg = 1
    for num in lines:
        contents.insert(num+flg, f"{new_string}")
        flg = flg + 1
    with open(filename, 'a') as f:
        f.writelines(contents)
