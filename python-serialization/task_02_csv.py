#!/usr/bin/env python3
"""
2. Converting CSV Data to JSON Format
"""

import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Convert CSV data to JSON format and save to data.json
    
    Args:
        csv_filename: Name of the CSV file to convert
        
    Returns:
        True if conversion successful, False otherwise
    """
    try:
        # Read CSV data
        data = []
        with open(csv_filename, 'r', encoding='utf-8') as csv_file:
            # Use DictReader to convert each row to a dictionary
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                data.append(row)
        
        # Serialize to JSON and write to file
        with open('data.json', 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)
        
        return True
        
    except FileNotFoundError:
        print(f"Error: File '{csv_filename}' not found.")
        return False
    except Exception as e:
        print(f"Error: {e}")
        return False
