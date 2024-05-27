#!/usr/bin/python3
"""Function that write into a file"""


def write_file(filename="", text=""):
    """Write a content into a file

        Args:
            filename (str): The name of the file to write to
            text (str): The content to write to the file
        Return:
            The number of character written to the file
    """
    with open(filename, mode="w", encoding="utf-8") as myFile:
        return myFile.write(text)
