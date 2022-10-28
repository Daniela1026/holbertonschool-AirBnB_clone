#!/usr/bin/python3
"""
Test Review
"""
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """"
    Test Review
    """

    def test_place_id(self):
        """
        Test at place id/atribute
        """
        rev = Review()
        self.asserEqual(rev.place_id, "")

    def test_user_id(self):
        """
        Test at user/atribute
        """
        rev = Review()
        self.asserEqual(rev.user_id, "")

    def test_txt(self):
        """
        Test at text/atribute
        """
        rev = Review()
        self.asserEqual(rev.txt, "")
