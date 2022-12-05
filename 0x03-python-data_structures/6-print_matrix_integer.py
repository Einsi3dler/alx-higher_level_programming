#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for arr in matrix:
        lim = len(arr)
        lim_1 = 0
        for num in arr:
            lim_1 = lim_1 + 1
            if lim == lim_1:
                print("{:d}".format(num), end="")
            else:
                print("{:d}".format(num), end=" ")
        print()
