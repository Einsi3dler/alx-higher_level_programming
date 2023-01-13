#!/usr/bin/python3
"""
This module contains a single function
"""


def pascal_triangle(n):
    """"
    this accepts an integer, spits out the pascal triangle till that int
    """
    if n <= 0:
        return []
    if n == 1:
        return [[1]]
    final_res = [[1]]
    res = [1]
    for x in range(1, n):
        flg = 0
        temp = []
        for val in res:
            temp.append(flg + val)
            flg = val
        temp.append(1)
        final_res.append(temp)
        res = temp
    return final_res
