#!/usr/bin/python3
"""
Module: 0-lookup
Contains function that returns attributes and methods of an object
"""


def lookup(obj):
    """
    Returns the list of available attributes and methods of an object
    
    Args:
        obj: Any Python object
        
    Returns:
        list: List of attribute and method names
    """
    return dir(obj)
