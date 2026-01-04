#!/usr/bin/python3
"""Module for printing squares with # characters."""


def print_square(size):
    """Prints a square of given size using # characters.

    Args:
        size: Length of the square sides (must be integer >= 0)

    Raises:
        TypeError: If size is not an integer
        ValueError: If size is negative
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
