#!/usr/bin/python3
"""Funtion that read a file"""


def read_file(filename=""):
    """Read and print the content of a utf-8 file"""
    with open(filename, encoding="utf-8") as myFile:
        print(myFile.read(), end="")