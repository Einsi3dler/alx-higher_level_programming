#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is None:
        return
    else:
        res_arr = []
        for sub_arr in matrix:
            res_arr.append(list(map(lambda x: x**2, sub_arr)))
        return res_arr
