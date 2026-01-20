#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in matrix:
        row = []
        for j in i:
            square = j ** 2
            row.append(square)
        new_matrix.append(row)
    return new_matrix
