#!/usr/bin/python3
"""
Module: 6-load_from_json_file
Contains function to load object from JSON file
"""
import json


def load_from_json_file(filename):
    """
    Creates an Object from a "JSON file"

    Args:
        filename (str): The name of the JSON file to load

    Returns:
        object: Python data structure loaded from the JSON file
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
