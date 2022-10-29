#!/usr/bin/python3
import unittest
from models.city import City


class CityTest(unittest.TestCase):
    def test_attribute(self):
        city = City()
        self.assertEqual(city.name, "")
        self.assertEqual(city.state_id, "")
