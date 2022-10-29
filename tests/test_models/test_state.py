#!/usr/bin/python3
"""
Test State
"""
import unittest
from models.state import State


class TestState(unittest.TestCase):

    def test_name_state(self):
        """Test attributes of Class State"""
        stt = State()
        self.assertEqual(stt.name, "")
