#!/usr/bin/python3
"""
Function that adds two integers
"""


def add_integer(a, b=98):
    """
    Returns the addition of a and b
    
    Args:
        a: first number (int or float)
        b: second number (int or float), defaults to 98
    
    Returns:
        Integer sum of a and b
    
    Raises:
        TypeError: If a or b is not int or float
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    
    # Convert floats to ints before addition
    return int(a) + int(b)
