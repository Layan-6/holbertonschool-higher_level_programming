#!/usr/bin/python3
"""
Module: 1-write_file
Contains function to write string to file and return character count
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF8) and returns 
    the number of characters written
    
    Args:
        filename (str): The name of the file to write to
        text (str): The text to write to the file
    
    Returns:
        int: Number of characters written
    """
    with open(filename, 'w', encoding='utf-8') as file:
        nb_chars = file.write(text)
        return nb_chars
