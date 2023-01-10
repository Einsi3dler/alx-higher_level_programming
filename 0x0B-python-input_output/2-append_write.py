#!/usr/bin/python3
"""
This contains a single function that appends files
"""
def append_write(filename="", text=""):
    with open(filename, 'a+', encoding="utf8") as f:
        data = f.write(text)
        return data
