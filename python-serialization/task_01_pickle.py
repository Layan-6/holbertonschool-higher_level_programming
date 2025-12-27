#!/usr/bin/env python3
"""
1. Picking Custom Classes
"""

import pickle

class CustomObject:
    def __init__(self, name: str, age: int, is_student: bool):
        """Initialize CustomObject with given attributes"""
        self.name = name
        self.age = age
        self.is_student = is_student
    
    def display(self):
        """Display object attributes in the required format"""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")
    
    def serialize(self, filename: str):
        """
        Serialize the current instance and save to file
        
        Args:
            filename: Name of the file to save to
            
        Returns:
            None if error occurs, otherwise nothing
        """
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except Exception:
            return None
    
    @classmethod
    def deserialize(cls, filename: str):
        """
        Deserialize an instance from file
        
        Args:
            filename: Name of the file to load from
            
        Returns:
            CustomObject instance or None if error occurs
        """
        try:
            with open(filename, 'rb') as f:
                return pickle.load(f)
        except Exception:
            return None
