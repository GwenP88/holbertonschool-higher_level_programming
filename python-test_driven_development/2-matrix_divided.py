#!/usr/bin/python3
def matrix_divided(matrix, div):
    message1 = "matrix must be a matrix (list of lists) of integers/floats"
    message2 = "Each row of the matrix must have the same size"

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not isinstance(matrix, list) or not matrix:
        raise TypeError(message1)

    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(message1)

    has_non_empty_row = False
    for row in matrix:
        if len(row) > 0:
            has_non_empty_row = True
            break

    if not has_non_empty_row:
        raise TypeError(message1)

    ref_size = None
    new_matrix = []

    for row in matrix:
        if ref_size is None and len(row) > 0:
            ref_size = len(row)

        if len(row) != ref_size:
            raise TypeError(message2)

        new_row = []
        for x in row:
            if not isinstance(x, (int, float)):
                raise TypeError(message1)
            new_row.append(round(x / div, 2))

        new_matrix.append(new_row)

    return new_matrix
