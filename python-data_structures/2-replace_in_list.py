#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    # Check if idx is valid (not negative and within range)
    if idx < 0 or idx >= len(my_list):
        return my_list
    # Replace the element at the given index
    my_list[idx] = element
    return my_list
