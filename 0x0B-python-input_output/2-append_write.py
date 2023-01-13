#!/usr/bin/python3
"""
This contains a single function that appends files
"""
def append_write(filename="", text=""):
    """
    this funciton accept text which is appended to file name
    """
    with open(filename, 'a+', encoding="utf8") as f:
        data = f.write(text)
        return data
