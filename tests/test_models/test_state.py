#!/usr/bin/python3
"""
Test State
"""
import unittest
from models.state import State



class Teststate(unittest.TestCase):

    def test_state(self):
        """
        Test attributes of Class State
        """
        my_state = State()
        self.assertEqual(my_state.name, "")
