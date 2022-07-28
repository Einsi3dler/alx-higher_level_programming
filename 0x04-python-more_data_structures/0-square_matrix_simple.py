#!/usr/bin/python3

def square_matrix_simple(matrix=[]):

    a = len(matrix) 

    dup_mat = [[]for x in range(a)] 

    i = 0
    for array in matrix:
        j = 0
        for num in array:
            a = matrix[i][j]
            a = a**2
            dup_mat[i].append(a)
            j = j + 1
        i = i + 1


    
    return (dup_mat)
