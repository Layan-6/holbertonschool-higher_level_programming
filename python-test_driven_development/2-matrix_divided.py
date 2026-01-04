#!/usr/bin/python3
"""Matrix division module"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by a number
    Args:
        matrix: List of lists of integers/floats
        div: Number to divide by (cannot be zero)
    Returns:
        New matrix with results rounded to 2 decimals
    Raises:
        TypeError: If matrix is invalid or div isn't number
        ZeroDivisionError: If div is zero
    """
    # Validate matrix structure
    if not isinstance(matrix, list) or \
       not all(isinstance(row, list) for row in matrix) or \
       not all(isinstance(num, (int, float)) for row in matrix for num in row):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )
    # Validate matrix is not empty
    if not matrix:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )
    # Validate uniform row size
    row_size = len(matrix[0])
    if any(len(row) != row_size for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    # Validate divisor
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    # Perform division and rounding
    return [[round(num / div, 2) for num in row] for row in matrix]
