#!/usr/bin/python3
"""
Test User
"""

import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """
    Test at user/class
    """

    def test_email(self):
        """Test at email/attribute"""
        us = User()
        self.assertEqual(us.email, "")

    def test_password(self):
        """Test at password/attribute"""
        us = User()
        self.assertEqual(us.password, "")

    def test_first_name(self):
        """Test at fitst_name/attribute"""
        us = User()
        self.assertEqual(us.first_name, "")

    def test_last_name(self):
        """Test at last_name/attribute"""
        us = User()
        self.assertEqual(us.last_name, "")
