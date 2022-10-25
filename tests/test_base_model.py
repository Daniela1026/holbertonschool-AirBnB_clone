#!/usr/bin/python3
""" """
import unittest
from models.base_model import BaseModel
from datetime import datetime

class TestBase(unittest.TestCase):

    def test_id(self):
        """ """
        t_base1 = BaseModel()
        self.assertIsInstance(t_base1, BaseModel)
        t_base2 = BaseModel()
        self.assertNotEqual(t_base1.id, t_base2.id)

    def test_created_at(self):
        """ """
        t_base1 = BaseModel()
        self.assertTrue(type(t_base1.created_at) == datetime)

    def test_updated_at(self):
        """ """
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_str(self):
        """ """
        t_model = BaseModel()
        t_model.my_number = 89
        t_model.name = "My First Model"
        t_dict = t_model.to_dict()
        self.assertIn('name', t_dict)
        self.assertIn('my_number', t_dict)
        self.assertIn('id', t_dict)
        self.assertIn('created_at', t_dict)
        self.assertIn('updated_at', t_dict)

    def test_save(self):
        """ """
        t_base1 = BaseModel()
        sleep(2)
        update = t_base1.updated_at
        t_base1.save()
        self.assertNotEqual(update, t_base1.updated_at)

    def test_to_dict(self):
        """ """
        t_base1 = BaseModel()
        self.assertTrue(dict, type(t_base1.to_dict))
