#!/usr/bin/python3
"""Generate Pascal's triangle of n as a list of lists"""


def pascal_triangle(n):
    """Return Pascal's triangle of n"""
    if n <= 0:
        return []
    triangle = [[1]]
    while len(triangle) < n:
        prev_line = triangle[-1]
        new_line = [1]
        for i in range(1, len(prev_line)):
            new_line.append(prev_line[i - 1] + prev_line[i])
        new_line.append(1)
        triangle.append(new_line)
    return triangle
