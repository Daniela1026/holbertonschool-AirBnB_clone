#!/usr/bin/python3
"""
Unitest Class BaseModel
"""
import unittest
import uuid
import json
import pycodestyle as pep8
import inspect
from datetime import datetime


class TestBase(unittest.TestCase):

    def test_pep8_base(self):
        """Test that checks for PEP8"""
        syntax = pep8.StyleGuide(quit=True)
        result = syntax.check_files(["models/base_model.py"])
        self.assertEqual(
            result.total_errors, 0, "Found code style errors (and warnings)."
        )

    def test_base_instance(self):
        """Checks if base_instance is a BaseModel instance"""
        self.assertIsInstance(base_instance, BaseModel)

    def test_save(self):
        t_base1 = BaseModel()
        created_at = t_base1.created_at
        update_at = t_base1.updated_at
        t_base1.save()
        self.assertNotEqual(update_at, t_base1.updated_at)
        self.assertEqual(created_at, t_base1.created_at)

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

    def test_save2(self):
        """
        Test to check each update in the storage
        """
        t_base1 = BaseModel()
        try:
            os.remove('file.json')
        except Exception:
            pass
        t_base1.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_to_dict(self):
        """
        Test the to_dict method from BaseModel
        """
        t_base1 = BaseModel()
        self.assertTrue(dict, type(t_base1.to_dict))

        if __name__ == '__main__':
            unittest.main()
