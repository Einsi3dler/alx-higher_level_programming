#!/usr/bin/python3
"""
This module contains one class
"""


class MyList(list):
    """
    This class contains a singlem function
    """
    def print_sorted(self):
        """
        this sorts the list
        """
        val = list.copy(self)
        list.sort(val)
        print(val)
