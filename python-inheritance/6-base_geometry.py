#!/usr/bin/python3
"""Defines BaseGeometry class with area method."""


class BaseGeometry:
    """Base geometry class with unimplemented area method."""

    def area(self):
        """Raise an exception indicating area() is not implemented.

        Raises:
            Exception: Always raises with message 'area() is not implemented'
        """
        raise Exception("area() is not implemented")
