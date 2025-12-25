#!/usr/bin/python3
"""
Module: 1-my_list
Contains class MyList that inherits from list
"""


class MyList(list):
    """
    MyList class that inherits from list
    
    Methods:
        print_sorted: prints the list in ascending sorted order
    """
    
    def print_sorted(self):
        """
        Prints the list in ascending sorted order
        
        Returns:
            None: just prints the sorted list
        """
        sorted_list = sorted(self)
        print(sorted_list)
