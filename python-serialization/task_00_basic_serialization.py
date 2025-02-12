/usr/bin/env python3
import json
import os

def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary to JSON and save it to a file.
    
    Args:
        data (dict): Python dictionary to be serialized
        filename (str): Name of the output JSON file
        
    Raises:
        TypeError: If data is not a dictionary
        IOError: If there's an error writing to the file
    """
    if not isinstance(data, dict):
        raise TypeError("Input data must be a dictionary")
    
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4)
    except IOError as e:
        raise IOError(f"Error writing to file {filename}: {str(e)}")

def load_and_deserialize(filename):
    """
    Load and deserialize JSON data from a file into a Python dictionary.
    
    Args:
        filename (str): Name of the input JSON file
        
    Returns:
        dict: Deserialized Python dictionary
        
    Raises:
        FileNotFoundError: If the specified file doesn't exist
        json.JSONDecodeError: If the file contains invalid JSON
        IOError: If there's an error reading the file
    """
    if not os.path.exists(filename):
        raise FileNotFoundError(f"File {filename} not found")
    
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return json.load(file)
    except json.JSONDecodeError as e:
        raise json.JSONDecodeError(f"Invalid JSON in file {filename}: {str(e)}", e.doc, e.pos)
    except IOError as e:
        raise IOError(f"Error reading file {filename}: {str(e)}")
