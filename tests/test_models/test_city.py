#!/usr/bin/python3
"""
Unittest module for the City Class
"""
import unittest
from models.city import City

class TestCity(unittest.TestCase):

    """Test Cases for the City class."""

    def test_state_id(self):
        """Tests the attributes of City class."""
        cit = City
        self.asserEqual(cit.state_id, "")

    def test_name_state(self):
        """Test the attributes of name City"""
        cit = City()
        self.aseertEqual(cit.name, "")
