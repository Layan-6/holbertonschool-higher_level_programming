#!/usr/bin/python3
"""
This module provides a function to add two integers.
"""


def add_integer(a, b=98):
    """
    Adds two integers.

    Args:
        a: first integer or float
        b: second integer or float (default 98)

    Returns:
        int: sum of a and b

    Raises:
        TypeError: if a or b is not integer or float
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
