#!/usr/bin/python3
"""Serialize and deserialize Python dictionaries to/from XML."""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serialize a dictionary to XML format.

    Args:
        dictionary (dict): The dictionary to serialize.
        filename (str): The name of the file to save the XML data.
    """
    root = ET.Element('data')

    for key, value in dictionary.items():
        child = ET.SubElement(root, str(key))
        child.text = str(value)

    tree = ET.ElementTree(root)

    tree.write(filename, encoding="utf-8", xml_declaration=True)

def deserialize_from_xml(filename):
    """
    Deserialize XML data from a file to a Python dictionary.

    Args:
        filename (str): The name of the XML file to deserialize.

    Returns:
        dict: The deserialized dictionary.
    """
    try:
        tree = ET.parse('filename')
        root = tree.getroot()

        deserialized_dict = {}
        for child in root:
            deserialized_dict[child.tag] = child.text

        return deserialized_dict

    except Exception as e:
        print(f"An error occurred: {e}")
        return None
