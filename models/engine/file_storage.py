#!/usr/bin/python3
"""
This module is meant to define the storage class
"""
import json
from os import path
from models.base_model import BaseModel
from models.user import User
from models.state import State

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
        Returns the dictionary __objects
        """
        return self.__objects"""

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id
        """
        Sets in __objects the obj with key <obj class name>.id
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)
        """
        Serializes __objects to the JSON file (path: __file_path)
        """
        dict_to_json = {}
        for k, v in FileStorage.__objects.items():
            dict_to_json[k] = v.to_dict()
        with open(FileStorage.__file_path, "w") as f:
            json.dump(dict_to_json, f)
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
            with open(FileStorage.__file_path, "r") as f:
                reader = json.load(f)
                for k, v in reader.items():
                    FileStorage.__objects[k] = eval(v['__class__'] + '(**v)')
        except Exception:
            pass
        if path.exist(self.__file__path):
            with open(self.__file__path, "r", encoding="utf-8") as file:
                json_object = json.loads(file.read())

            for key, value in json_object.items():
                self.__onjects[key] = eval (value['__class__'])(**value)
