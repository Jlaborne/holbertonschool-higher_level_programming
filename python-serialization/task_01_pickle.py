#!/usr/bin/python3
"""Define a class CustomObject"""
import json
import pickle


class CustomObject:
    """Represent an CustomObject"""
    def __init__(self, name, age, is_student):
        """Initialize the CustomObject with name, age, is_student attributes
        
        Args:
            name (str): The name of the person
            age (str): The age of the person
            is_student (bool): Is student or not
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Print the object's attributes """

        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is student: {self.is_student}")

    def serialize(self, filename):
        """Serialize the instance of the object into provided file
        
        Args:
            filename (str): The provided filename
        """
        try:
            with open(filename, 'wb') as myFile:
                pickle.dump(self, myFile)
        except:
            print("Non-existant or malformed files")

    @classmethod
    def deserialize(cls, filename):
        """Load and return an instance of the object from filename

        Args:
            filename (str): The filename to load

        Return:
            CustomObject: The deserialized object, or None if an error occurs
        """
        try:
            with open(filename, 'rb') as myFile:
                return pickle.load(myFile)
        except:
            print("Non-existant or malformed file")
            return None
