#!/usr/bin/python3
"""
This module defines a custom list class that inherits from the built-in list.

"""


class MyList(list):
    """
    A subclass of list.
    """

    def print_sorted(self):
        """
        Prints the elements of the list in ascending sorted order.

        """
        print(sorted(self))
