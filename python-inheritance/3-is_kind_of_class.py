#!/usr/bin/python3
"""
This module defines a function that checks if an object
is an instance of a class or a subclass.
"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if the object is an instance of the specified class,
    or if it is an instance of a class that inherited from it.

    Args:
        obj: Any object.
        a_class: The class to check against.

    Returns:
        True if obj is an instance or inherited of a_class, else False.
    """
    return isinstance(obj, a_class)
