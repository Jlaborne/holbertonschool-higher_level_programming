#!/usr/bin/python3
import json
"""Module that add the functionality to serialize a Python dictionary to a JSON file
    and deserialize a JSON file to recreate a Python dictionary
"""


def serialize_and_save_to_file(data, filename):
    """Python dictionary to json file
    
    Args:
        data (dict): The dictionary to serialize
        filename (str): The filename of the output JSON file
    """
    with open(filename, "w") as myFile:
        json.dump(data, myFile)

def load_and_deserialize(filename):
    """Load and deserialize JSON data from a file to python dictionary
    
    Args:
        filename (str): The filename of the input file

    Return:
        dict: The deserialized Python dictionary
    """
    with open(filename, "r") as myFile:
        data = json.load(myFile)
    return data
