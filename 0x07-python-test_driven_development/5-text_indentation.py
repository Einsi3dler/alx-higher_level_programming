#!/usr/bin/python3
"""
This module contains a function that indents file
"""


def text_indentation(text):
    if type(text) != str:
        raise TypeError("text must be a string")
    begin = 0
    end = 0
    str_len = len(text)
    for char in text:
        if char in ['.', '?', ':']:
            print(text[begin:end+1].strip())
            print()
            begin = end + 1
        end = end + 1
    if str_len != begin:
        print("{}".format(text[begin:str_len].strip()), end="")
