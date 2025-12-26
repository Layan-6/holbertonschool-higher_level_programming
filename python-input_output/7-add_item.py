#!/usr/bin/python3
"""
Module: 7-add_item
Script that adds all arguments to a Python list and saves to file
"""
import sys
import os

# Import the required functions
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def main():
    """
    Main function to add arguments to list and save to file
    """
    filename = "add_item.json"
    
    # Load existing list or create new one
    if os.path.exists(filename):
        try:
            items = load_from_json_file(filename)
        except Exception:
            items = []
    else:
        items = []
    
    # Add command line arguments (excluding script name)
    items.extend(sys.argv[1:])
    
    # Save the updated list
    save_to_json_file(items, filename)


if __name__ == "__main__":
    main()
