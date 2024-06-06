#!/usr/bin/python3
from .base_model import BaseModel


class City(BaseModel):
    def __init__(self, name, country=None):
        super().__init__()
        self.name = name
        self.country = country
        self.places = []

    def add_place(self, place):
        self.places.append(place)
        place.city = self

    def to_dict(self):
        dict_representation = super().to_dict()
        dict_representation['country'] = self.country.to_dict() if self.country else None
        dict_representation['places'] = [place.to_dict() for place in self.places]
        return dict_representation