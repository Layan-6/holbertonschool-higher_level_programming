#!/usr/bin/python3
"""
Module: task_00_basic_serialization
Basic serialization module for JSON operations
"""
import json


def serialize_and_save_to_file(data, filename):
    """
    Serializes a Python dictionary to JSON and saves it to a file

    Args:
        data (dict): Python Dictionary with data
        filename (str): The filename of the output JSON file
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file)


def load_and_deserialize(filename):
   
