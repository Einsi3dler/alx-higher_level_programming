#!/usr/bin/python3
"""
This module contains a doc that writes to files
"""


def write_file(filename="", text=""):
    """
    writes data to a file, creates the file if it's not there
    """
    with open(filename, 'w+', encoding="utf-8") as f:
        data = f.write(text)
        return data
