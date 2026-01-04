#!/usr/bin/python3
"""better rectangle"""
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

    def area(self):
        """area

        Return: rectangle area
        """
        return self.__width * self.__height

    def __str__(self):
        """represent rectangle

        Return: string format
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
