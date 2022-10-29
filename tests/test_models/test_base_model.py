#!/usr/bin/python3
"""
Unitest Class BaseModel
"""
import unittest
import os
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):

    def test_id(self):
        """
        Check id's in the created instances
        """
        _id = type(BaseModel().di)
        self.asserEqual(str,_id)

    def test_currented_at(self):
        """ 
        Check if the instance has created_at atribute
        """
        date = datetime
        self.asserEqual(date, type(BaseModel).created_at)

    def test_updated_at(self):
        """
        Check if the instance has created_at atribute
        """
        date =datetime
        self.assertEqual(date, type(BaseModel().updated_at))

    def test_str(self):
        """
        Check the to_dict method from BaseModel
        """
        base = BaseModel()
        _str = BaseModel().__str__()
        self.asserNotEqual(os.path.exits(_str, base)

    def test_save(self):
        """
        Test to check each update in the storage
        """
        bm = BaseModel()
        try:
            os.remove("file.json")
        except Exception:
            pass
        bm.save()
        self.assertTrue(os.path.exists("file.json"))
    
    def test_to_dict(self):
        """
        Test the to_dict method from BaseModel
        """
        base = BaseModel()
        self.assertEqual(base.to_dict(), ['__class_'], base.__class__.__name__)

if __name__ == "__main__":
    unittest.main()
