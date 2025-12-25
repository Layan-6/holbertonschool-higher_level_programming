#!/usr/bin/python3
"""
Module: 0-read_file
Contains function to read and print text file
"""


def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints it to stdout
    
    Args:
        filename (str): The name of the file to read
    """
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
        print(content, end='')
