#!/usr/bin/python3
"""Function that append into a file"""


def write_file(filename="", text=""):
    """Append a content into a file

        Args:
            filename (str): The name of the file to append to
            text (str): The content to append to the file
        Return:
            The number of character added to the file
    """
    with open(filename, mode="a", encoding="utf-8") as myFile:
        return myFile.write(text)
