#!/usr/bin/python3
"""
Test Amenity
"""
import unittest
from models. amenity import Amenity


class Testamenity(unittest.TestCase):

    def test_amenity(self):
        """
        Test attributes of Class Amenity
        """
        nm = Amenity()
        self.assertEqual(nm.name, "")
