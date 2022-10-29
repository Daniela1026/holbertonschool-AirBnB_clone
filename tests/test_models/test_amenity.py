#!/usr/bin/python3
"""
Test Amenity
"""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):

    def test_name(self):
        """Test attributes or class Amenity"""
        am = Amenity()
        self.assertEqual(am.name, "")
