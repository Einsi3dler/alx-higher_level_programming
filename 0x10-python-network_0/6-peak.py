#!/usr/bin/python3
""" function to find the number peak"""


def find_peak(list_of_integers):
    """ The function"""
    if len(list_of_integers) == 0:
        return None
    else:
        list_of_integers.sort()
        return list_of_integers.pop()
