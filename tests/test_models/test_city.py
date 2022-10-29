#!/usr/bin/python3
<<<<<<< HEAD
=======
"""
Test City
"""
>>>>>>> b10ecae2e846e3f7ca5fc11a3d609585d5ca13ee
import unittest
from models.city import City


<<<<<<< HEAD
class CityTest(unittest.TestCase):
    def test_attribute(self):
        city = City()
        self.assertEqual(city.name, "")
        self.assertEqual(city.state_id, "")
=======
class TestCity(unittest.TestCase):
    """
    Test city
    """

    def test_state_id(self):
        """
        Test at id/attribute
        """
        cit = City()
        self.assertEqual(cit.state_id, "")

    def test_name_state(self):
        """
        Test at name/attribute
        """
        cit = City()
        self.assertEqual(cit.name, "")
>>>>>>> b10ecae2e846e3f7ca5fc11a3d609585d5ca13ee
