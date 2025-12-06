#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i, num in enumerate(row):
            # Use format to print integer
            print("{:d}".format(num), end="")
            # Don't print space after last element in row
            if i != len(row) - 1:
                print(" ", end="")
        print()
