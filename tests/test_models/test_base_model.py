#!/usr/bin/python3
""" """
import unittest
import uuid
from datetime import datetime
from models import base_model
BaseModel = base_model.BaseModel

class TestBase(unittest.TestCase):

    def test_save(self):
        t_base1 = BaseModel()
        created_at = t_base1.created_at
        update_at = t_base1.updated_at
        t_base1.save()
        self.assertNotEqual(update_at, t_base1.updated_at)
        self.assertEqual(created_at, t_base1.created_at)

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
        try:
            os.remove('file.json')
        except Exception:
            pass
        t_base1.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_to_dict(self):
        """ """
        t_base1 = BaseModel()
        self.assertTrue(dict, type(t_base1.to_dict))
