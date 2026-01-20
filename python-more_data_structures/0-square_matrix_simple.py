#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for values in matrix:
        row = []
        for value in values:
            square = value ** 2
            row.append(square)
        new_matrix.append(row)
    return new_matrix
