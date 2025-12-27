#!/usr/bin/env python3
"""
0. Basic Serialization
"""

import json

def serialize_and_save_to_file(data, filename):
    """
    Serializes a Python dictionary to a JSON file.
    
    Args:
        data: Python dictionary to serialize
        filename: Name of the output JSON file
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f)

def load_and_deserialize(filename):
    """
    Loads and deserializes JSON data from a file.
    
    Args:
        filename: Name of the JSON file to read
        
    Returns:
        Python dictionary with the deserialized data
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)

# Example test code (might be required or might not)
if __name__ == "__main__":
    # Sample data
    data_to_serialize = {
        "name": "John",
        "age": 30,
        "city": "New York"
    }
    
    # Serialize
    serialize_and_save_to_file(data_to_serialize, "data.json")
    print("Data serialized and saved to data.json")
    
    # Deserialize
    deserialized_data = load_and_deserialize("data.json")
    print("Deserialized Data:", deserialized_data)
