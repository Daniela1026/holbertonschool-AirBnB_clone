#!/usr/bin/python3
"""
This module is meant to define the storage class
"""
import json
from os import path
from models.user import User
from models.state import State
from models.base_model import BaseModel

class FileStorage:
    """
    Serializes instances to a JSON file and deserializes JSON file to
    instances
    FileStorage class module
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)
        """
        dict_to_json = {}
        for key, value in self.__objects.items():
            dict_json[key] = value.to_dict()
        with open(self.__file_path, "w", encoding="utf-8") as file:
            json.write(json.dumps(dict_json))

    def reload(self):
        """Deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists ; otherwise, do nothing. If the file doesn’t
        exist, no exception should be raised)
        """
        try:
            with open(self.__file_path, "r", encoding="utf-8") as file:
                file_dict = json.load(file)
                for key, value in file_dict.items():
                    value = eval(value["__class__"])(**value)
                    self.__objects[key] = value
        except:
            pass
