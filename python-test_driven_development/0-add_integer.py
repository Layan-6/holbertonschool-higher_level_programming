#!/usr/bin/python3
"""

This module provides a function that add two inegers,

It that both arguments are integers or floats, cast floats to integer.
"""


def add_integer(a, b=98):

    """
    Add two integer.

    Args:
        a: The first number.
        bL defaults to 98.

    Returns:
        int: The sum of the two integer>

    Rasies:
        TypeError: If a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
