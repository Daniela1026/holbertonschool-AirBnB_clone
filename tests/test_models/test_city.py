#!/usr/bin/python3
"""
Test City
"""
import unittest
from models.city import City


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
