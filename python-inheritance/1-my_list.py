class MyList(list):
    """
    MyList class that inherits from list.
    Adds a method to print the list in sorted order.
    """

    def print_sorted(self):
        """
        Prints the list in ascending sorted order.
        Does not modify the original list.
        """
        sorted_list = sorted(self)
        print(sorted_list)
