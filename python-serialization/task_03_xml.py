#!/usr/bin/env python3
"""
3. Serializing and Deserializing with XML
"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary to XML
    
    Args:
        dictionary: Python dictionary to serialize
        filename: Name of the XML file to create
        
    Returns:
        None
    """
    try:
        # Create root element
        root = ET.Element("data")
        
        # Iterate through dictionary items
        for key, value in dictionary.items():
            # Convert value to string since XML stores everything as text
            child = ET.SubElement(root, key)
            child.text = str(value)
        
        # Create element tree and write to file
        tree = ET.ElementTree(root)
        tree.write(filename, encoding='utf-8', xml_declaration=True)
        
    except Exception as e:
        print(f"Error serializing to XML: {e}")


def deserialize_from_xml(filename):
    """
    Deserialize XML file to Python dictionary
    
    Args:
        filename: Name of the XML file to read
        
    Returns:
        Python dictionary with the deserialized data
    """
    try:
        # Parse the XML file
        tree = ET.parse(filename)
        root = tree.getroot()
        
        # Reconstruct dictionary from XML elements
        result_dict = {}
        for child in root:
            result_dict[child.tag] = child.text
        
        return result_dict
        
    except Exception as e:
        print(f"Error deserializing from XML: {e}")
        return None
