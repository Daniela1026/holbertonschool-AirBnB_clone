#!/usr/bin/python3
"""
Test Review
"""
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """
    Test Review
    """

    def test_place_id(self):
        """Test at place_id/attribute"""
        rew = Review()
        self.assertEqual(rew.place_id, "")

    def test_user_id(self):
        """Test at user_id/attribute"""
        rew = Review()
        self.assertEqual(rew.user_id, "")

    def test_text(self):
        """Test at text/attribute"""
        rew = Review()
        self.assertEqual(rew.text, "")
