#!/usr/bin/python3
"""Unittest module for the Review Class."""

import unittest
from models.review import Review

class TestReview(unittest.TestCase):
    """Test Cases for the Review class."""

    def test_place_id(self):
        """Tests instantiation of Review class."""
        rew = Review()
        self.asserEqual(rew.place_id, "")

    def test_user_id(self):
        """Test at user_id/attribute"""
        rew = Review()
        self.asserEqual(rew.user_id, "")

    def test_text(self):
        """Test at text/attribute"""
        rew = Review()
        self.asserEqual(rew.text, "")
