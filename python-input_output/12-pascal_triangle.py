#!/usr/bin/python3
"""
Module: 12-pascal_triangle
Contains function to generate Pascal's triangle
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing Pascal's triangle of n

    Args:
        n (int): Number of rows for Pascal's triangle

    Returns:
        list: List of lists representing Pascal's triangle
    """
    if n <= 0:
        return []

    triangle = [[1]]  # First row is always [1]

    for i in range(1, n):
        prev_row = triangle[-1]
        new_row = [1]  # First element is always 1

        for j in range(1, i):
            # Each element is sum of two elements above it
            new_value = prev_row[j - 1] + prev_row[j]
            new_row.append(new_value)

        new_row.append(1)  # Last element is always 1
        triangle.append(new_row)

    return triangle
