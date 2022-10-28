#!/usr/bin/python3
"""
Test City
"""
import unittest
from models.city import City


class Testcity(unittest.TestCase):

    """
    Test city
    """

    def test_state_id(self):
        """
        Test at id/atribute
        """
        city = City
        self.asserEqual(city.state_id, "")

    def test_name_state(self):
        """
        Test at name/atribute
        """
        city = City()
        self.asserEqual(city.name, "")
