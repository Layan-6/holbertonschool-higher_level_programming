#!/usr/bin/python3
"""
Module 2-rectangle
Defines a Rectangle class with width, height, area, and perimeter methods.
"""


class Rectangle:
    """Represents a rectangle with private width and height attributes."""

    def __init__(self, width=0, height=0):
        """Initializes a new Rectangle with width and height.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieves the width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width while enforcing validation.

        Args:
            value (int): New width value.

        Raises:
            TypeError: If width is not an integer.
            ValueError: If width is < 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height while enforcing validation.

        Args:
            value (int): New height value.

        Raises:
            TypeError: If height is not an integer.
            ValueError: If height is < 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates and returns the rectangle's area."""
        return self.__width * self.__height

    def perimeter(self):
        """Calculates and returns the rectangle's perimeter.

        Returns:
            If width or height is 0, returns 0. Otherwise, returns perimeter.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
