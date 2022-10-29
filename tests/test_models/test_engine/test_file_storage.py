#!/usr/bin/python3
"""
Unit tests for file storage
"""
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from os import path


class TestFileStorage(unittest.TestCase):

    def test_filepath(self):
    """Test if module file_storage has documentation"""
        s = FileStorage()
        storage = s._FileStorage__file_path
        self.assertEqual(storage, "file.json")

<<<<<<< HEAD
    def test_all_method(self):
    """Test all method"""
=======
    def test_all(self):
        """Test all method"""
>>>>>>> 29bbad0cefb06d87f6c4bc04f7e0988a8c27dc42
        storage = FileStorage()
        self.assertEqual(type(storage.all()), dict)
        self.assertIs(storage.all(), storage._FileStorage__objects)

    def test_reload(self):
    """Test Reload Method"""
        storage = FileStorage()
        storage.save()
        storage.reload()
        self.assertTrue(len(storage.all()) > 0)
