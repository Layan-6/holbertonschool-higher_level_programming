#!/usr/bin/python3
"""rectangle stuff"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """making some rectangles"""

    def __init__(self, width, height):
        """instantiate

        Args:
          width (int): width
          height (int): height
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
