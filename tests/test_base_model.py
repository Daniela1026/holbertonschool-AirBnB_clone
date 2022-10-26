#!/usr/bin/python3
"""
Unitest Class BaseModel
"""
import unittest
from models.base_model import BaseModel, __doc__ as mrdoc
import inspect
# importpep8
import models
from datetime import datetime

class TestBase(unittest.TestCase):
    """
    Unitest at testing
    """
    def test_id(self):
        """
        Check id's in the created instances
        """
        t_base1 = BaseModel()
        self.assertIsInstance(t_base1, BaseModel)
        t_base2 = BaseModel()
        self.assertNotEqual(t_base1.id, t_base2.id)

    def test_created_at(self):
        """ 
        Check if the instance has created_at atribute
        """
        t_base1 = BaseModel()
        self.assertTrue(type(t_base1.created_at) == datetime)

    def test_updated_at(self):
        """
        Check if the instance has created_at atribute
        """
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_str(self):
        """
        Check the to_dict method from BaseModel
        """
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
        """
        Test to check each update in the storage
        """
        t_base1 = BaseModel()
        sleep(2)
        update = t_base1.updated_at
        t_base1.save()
        self.assertNotEqual(update, t_base1.updated_at)

    def test_to_dict(self):
        """
        Test the to_dict method from BaseModel
        """
        t_base1 = BaseModel()
        self.assertTrue(dict, type(t_base1.to_dict))
