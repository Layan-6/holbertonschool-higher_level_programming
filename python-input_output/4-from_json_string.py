#!/usr/bin/python3
"""
Module: 4-from_json_string
Contains function to convert JSON string to Python object
"""
import json


def from_json_string(my_str):
    """
    Returns an object (Python data structure) represented by a JSON string

    Args:
        my_str (str): The JSON string to convert

    Returns:
        object: Python data structure represented by the JSON string
    """
    return json.loads(my_str)
