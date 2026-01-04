#!/usr/bin/python3
"""Module for printing formatted names."""


def say_my_name(first_name, last_name=""):
    """Prints 'My name is <first_name> <last_name>'.

    Args:
        first_name: First name string (required)
        last_name: Last name string (optional)

    Raises:
        TypeError: If names aren't strings or missing first_name
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
