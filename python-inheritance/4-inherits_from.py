#!/usr/bin/python3
"""
This module defines a function that checks if an object
is an instance of a subclass of a given class.
"""


def inherits_from(obj, a_class):
    """
    Returns True if obj is an instance of a class that inherited
    from a_class, but not if it's an instance of a_class itself.

    Args:
        obj: Any object.
        a_class: The class to check inheritance from.

    Returns:
        True if obj is an instance of a subclass of a_class, otherwise False.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
