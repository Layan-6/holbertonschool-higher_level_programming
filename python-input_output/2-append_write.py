#!/usr/bin/python3
"""
Module: 2-append_write
Contains function to append string to file and return character count
"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file (UTF8) and and
returns the number of characters added

    Args:
        filename (str): The name of the file to append to
        text (str): The text to append to the file

    Returns:
        int: Number of characters added
    """
    with open(filename, 'a', encoding='utf-8') as file:
        nb_chars = file.write(text)
        return nb_chars
