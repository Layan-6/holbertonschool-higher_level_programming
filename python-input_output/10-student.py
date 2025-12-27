#!/usr/bin/python3
"""
Module: 10-student
Defines a Student class with filtered to_json method
"""


class Student:
    """
    Student class that defines a student
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance

        Args:
            first_name (str): Student's first name
            last_name (str): Student's last name
            age (int): Student's age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance

        Args:
            attrs (list): List of attribute names to include (optional)

        Returns:
            dict: Dictionary representation of the student
        """
        # Get all attributes of the object
        obj_dict = self.__dict__

        # If attrs is provided and is a list of strings
        if isinstance(attrs, list) and all(isinstance(item, str) for item in attrs):
            # Filter dictionary to include only specified attributes
            result = {}
            for key, value in obj_dict.items():
                if key in attrs and isinstance(value, (list, dict, str, int, bool)):
                    result[key] = value
            return result
        else:
            # Return all serializable attributes
            result = {}
            for key, value in obj_dict.items():
                if isinstance(value, (list, dict, str, int, bool)):
                    result[key] = value
            return result
