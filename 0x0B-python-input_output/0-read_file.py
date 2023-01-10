#!/usr/bin/python3
"""
This module contains a singular function that reads files
"""


def read_file(filename=""):
    """
    This function accepts a single argument, the file name
    """
    with open(filename, encoding="utf-8") as f:
        data = f.read()
        for line in data:
            print(line, end="")
