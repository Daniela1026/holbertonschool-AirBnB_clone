#!/usr/bin/python3
"""
Test Place
"""
import unittest
from models.place import Place


class TestPlace(inittest.TestCase)
    """ 
    Test Place
    """

    def test_city_id(self):
        """
        Test at city/atribute/id
        """
        pla = Place()
        self.assertEqual(pla.city_id, "")

    def test_user_id(self):
        """
        Test at user/atribute/id
        """
        pla = Place()
        self.asserEqual(pla.user_id, "")

    def test_name(self):
        """
        Test at name/atribute
        """
        pla = Place()
        self.asserEqueal(pla.number_rooms, 0)

    def test_description(self):
        """
        Test at description/atribute
        """
        pla = Place()
        self.asserEqueal(pla.description, "")

    def test_num_rooms(self):
        """
        Test at number/rooms
        """
        pla = Place()
        self.asserEqueal(pla.number_rooms, 0)

    def test_num_bathrooms(self):
        """
        Test at number bathrooms/atribute
        """
        pla = Place()
        self.asserEqueal(pla.number_bathrooms, 0)

    def test_max_guest(self):
        """
        Test at number max the guest/atribute
        """
        pla = Place()
        self.asserEqual(pla.max_guest, 0)

    def test_price_nigth(self):
        """
        Test at price to nigth/atribute
        """
        pla = Place
        self.asserEqual(pla.test_price_nigth, 0)

    def test_latitud(self)
        """
        Test at latitude/atribute
        """
        pla = Place()
        self.asserEqueal(pla.test_latitud, 0.0)

    def test_amenity_id(self):
        """
        Test at amenity id/atribute
        """
        pla = Place()
        self.asserEqual(pla.amenity_id, [])

