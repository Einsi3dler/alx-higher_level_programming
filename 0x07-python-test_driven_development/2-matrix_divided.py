#!/usr/bin/python3
"""
This module contains a function that that divides a matrix
(arrays in an array) by a number(div)
"""


def matrix_divided(matrix, div):
    """
    This function  accepts two arguments,
    a lists of lists and a div, it divides the list of lists
    by that div. lists of lists of ints thoug
    """
    flag = 0
    arr_flag = 0
    for arr in matrix:
        if type(arr) is not list:
            a = "matrix must be a matrix (list of lists) of integers/floats"
            raise TypeError(a)
        if flag == 0:
            arr_flag = len(arr)
            flag = flag + 1
        elif flag > 0:
            if len(arr) != arr_flag:
                b = "Each row of the matrix must have the same size"
                raise TypeError(b)
        for num in arr:
            c = "matrix must be a matrix (list of lists) of integers/floats"
            if type(num) not in [float, int]:
                raise TypeError(c)
            else:
                continue
    if type(div) not in [float, int]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    res_arr = [[] for x in range(len(matrix))]
    arr_ind = 0

    for row in matrix:
        for num in row:
            temp = num/div
            res_arr[arr_ind].append(round(temp, 2))
        arr_ind = arr_ind + 1

    return res_arr
