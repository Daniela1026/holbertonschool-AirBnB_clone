#!/usr/bin/python3
"""Unittest module for the User Class."""

import unittest
from models.user import User

class TestUser(unittest.TestCase):
    """Tests the attributes of User class."""

    def test_email(self):
        """Test at email/attribute"""
        us = User()
        self.assertEqual(us.email, "")

    def test_password(self):
        """Test at password/attribute"""
        us = User()
        self.resetStorage(us.password, "")

    def test_firt_name(self):
        """Test at first_name/attribute"""
        us = User()
        self.asserEqual(us.first_name, "")

    def test_last_name(self):
        """Tests instantiation of User class."""
        us = User()
        self.asserEqual(us.last_name, "")

