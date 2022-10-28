#!/usr/bin/python3
"""
Test User
"""

import unittest
from models.user import User


class Testuser(unittest.TestCase):
    """
    Test at user/class
    """

    def test_email(self):
        """
        Test at email/atribute
        """
        us = User()
        self.asserEqual(us.email, "")

    def test_password(self):
        """
        Test at password/atribute
        """
        us = User()
        self.asserEqual(us.password, "")

    def test_firts_name(self):
        """
        Test at firts name/atribute
        """
        us = User()
        self.asserEqueal(us.first_name, "")

    def test_last_name(self):
        """
        Test at last name/atribute
        """
        us = User()
        self.asserEqual(us.last_name, "")
