#!/usr/bin/python3
"""
Module: 9-student
Defines a Student class with to_json method
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

    def to_json(self):
        """
        Retrieves a dictionary representation of a Student instance

        Returns:
            dict: Dictionary representation of the student
        """
        obj_dict = self.__dict__
        result = {}
        for key, value in obj_dict.items():
            if isinstance(value, (list, dict, str, int, bool)):
                result[key] = value
        return result
