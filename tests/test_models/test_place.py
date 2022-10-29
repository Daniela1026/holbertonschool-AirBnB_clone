#!/usr/bin/python3
"""
Test Place
"""
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """
    Test Place
    """

    def test_city_id(self):
        """
        Test at city/attribute
        """
        pla = Place()
        self.assertEqual(pla.city_id, "")

    def test_user_id(self):
        """Test at id/attribute"""
        pla = Place()
        self.assertEqual(pla.user_id, "")

    def test_name(self):
        """Test at name/attribute"""
        pla = Place()
        self.assertEqual(pla.name, "")

    def test_description(self):
        """Test at description/attribute"""
        pla = Place()
        self.assertEqual(pla.description, "")

    def test_num_rooms(self):
        """Test at number/rooms"""
        pla = Place()
        self.assertEqual(pla.number_rooms, 0)

    def test_num_bathrooms(self):
        """Test at bathrooms/attribute"""
        pla = Place()
        self.assertEqual(pla.number_bathrooms, 0)

    def test_max_guest(self):
        """Test at max_guest/attribute"""
        pla = Place()
        self.assertEqual(pla.max_guest, 0)

    def test_price_by_night(self):
        """Test at price_by_night/attribute"""
        pla = Place()
        self.assertEqual(pla.price_by_night, 0)

    def test_latitude(self):
        """Test at latitude/attribute"""
        pla = Place()
        self.assertEqual(pla.latitude, 0.0)

    def test_longitude(self):
        """Test at longitude/attribute"""
        pla = Place()
        self.assertEqual(pla.longitude, 0.0)

    def test_amenity_ids(self):
        """Test at amenity_ids/attribute"""
        pla = Place()
        self.assertEqual(pla.amenity_ids, [])
