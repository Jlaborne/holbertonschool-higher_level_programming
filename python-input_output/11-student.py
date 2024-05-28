#!/usr/bin/python3
"""Define a Student class"""


class Student:
    """Represent a student"""
    def __init__(self, first_name, last_name, age):
        """Initialize a new student

        Args:
            first_name (str):
            last_name (str):
            age (int):
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get a dictionary representation of the student

        Args:
            attrs (list): attribute to represent
        """
        if (isinstance(attrs, list) and
                all(isinstance(ele, str) for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attribute of an object Student

        Args:
            json (dict): the key to replace values
        """
        for k, a in json.items():
            setattr(self, k, a)
