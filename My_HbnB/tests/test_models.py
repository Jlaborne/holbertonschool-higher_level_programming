# tests/test_models.py

import unittest
from classes.country import Country
from classes.city import City
from classes.amenity import Amenity
from classes.place import Place

class TestModels(unittest.TestCase):
    def test_country_creation(self):
        country = Country("Test Country")
        self.assertEqual(country.name, "Test Country")

    def test_city_creation(self):
        country = Country("Test Country")
        city = City("Test City", country)
        self.assertEqual(city.name, "Test City")
        self.assertEqual(city.country.name, "Test Country")

    def test_amenity_creation(self):
        amenity = Amenity("Test Amenity")
        self.assertEqual(amenity.name, "Test Amenity")

    def test_place_creation(self):
        country = Country("Test Country")
        city = City("Test City", country)
        place = Place("Test Place", city)
        self.assertEqual(place.name, "Test Place")
        self.assertEqual(place.city.name, "Test City")

if __name__ == '__main__':
    unittest.main()