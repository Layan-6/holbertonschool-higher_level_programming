#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    # Check if idx is valid
    if idx < 0 or idx >= len(my_list):
        return my_list
    
    # Create a new list without the element at idx
    new_list = []
    for i in range(len(my_list)):
        if i != idx:
            new_list.append(my_list[i])
    return new_list
