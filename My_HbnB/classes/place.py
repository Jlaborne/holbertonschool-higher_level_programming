#!/usr/bin/python3
from .base_model import BaseModel

class Place(BaseModel):
    def __init__(self, name, description, city):
        super().__init__()
        self.name = name
        self.description = description
        self.city = city
        city.add_place(self)