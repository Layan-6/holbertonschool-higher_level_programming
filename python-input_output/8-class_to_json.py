#!/usr/bin/python3
"""
Module: 8-class_to_json
Contains function to get dictionary description for JSON serialization
"""


def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure
    for JSON serialization of an object

    Args:
        obj: An instance of a Class

    Returns:
        dict: Dictionary with serializable attributes
    """
    # Get all attributes of the object
    obj_dict = obj.__dict__
    
    # Filter only serializable types
    result = {}
    for key, value in obj_dict.items():
        if isinstance(value, (list, dict, str, int, bool)):
            result[key] = value
    
    return result
