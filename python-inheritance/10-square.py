#!/usr/bin/python3
"""square stuff"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """square class"""

    def __init__(self, size):
        """

        Args:
           size(int): size of the side
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """

        Return: the area
        """
        return self.__size ** 2
