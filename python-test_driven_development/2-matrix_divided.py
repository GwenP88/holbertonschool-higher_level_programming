#!/usr/bin/python3
"""
Module: 2-matrix_divided

This module provides a function to divide all elements of a matrix
by a given number and return a new matrix with the results rounded
to two decimal places.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given number.

    The function returns a new matrix where each element is the result
    of dividing the corresponding element of the input matrix by div,
    rounded to two decimal places.

    Args:
        matrix (list of lists): A matrix of integers or floats.
        div (int or float): The number by which to divide each element
            of the matrix.

    Raises:
        TypeError: If matrix is not a list of lists of integers or floats.
        TypeError: If each row of the matrix does not have the same size.
        TypeError: If div is not a number.
        ZeroDivisionError: If div is equal to zero.

    Returns:
        list of lists: A new matrix with each element divided by div and
        rounded to two decimal places.
    """
    # Messages d'erreur attendus par les tests
    message1 = "matrix must be a matrix (list of lists) of integers/floats"
    message2 = "Each row of the matrix must have the same size"

    # Validation de div (type + division par zéro)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Validation de base de matrix (doit être une liste non vide)
    if not isinstance(matrix, list) or not matrix:
        raise TypeError(message1)

    # Validation : chaque ligne doit être une liste
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(message1)

    # Validation : la matrix ne doit pas être composée que de lignes vides
    has_non_empty_row = False
    for row in matrix:
        if len(row) > 0:
            has_non_empty_row = True
            break
    if not has_non_empty_row:
        raise TypeError(message1)

    # Référence de taille + construction de la nouvelle matrice
    ref_size = None
    new_matrix = []

    for row in matrix:
        # Définition de lataille_ref à partir de la première ligne non vide
        if ref_size is None and len(row) > 0:
            ref_size = len(row)

        # Vérification : toutes les lignes doivent avoir la même taille
        if len(row) != ref_size:
            raise TypeError(message2)

        # Division + arrondi de chaque élément
        new_row = []
        for x in row:
            if not isinstance(x, (int, float)):
                raise TypeError(message1)
            new_row.append(round(x / div, 2))

        new_matrix.append(new_row)

    return new_matrix
