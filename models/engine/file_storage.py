#!/usr/bin/python3
"""
This module is meant to define the storage class
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """
    Serializes instances to a JSON file and deserializes JSON file to
    instances
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
        for k, v in FileStorage.__objects.items():
            dict_to_json[k] = v.to_dict()
        with open(FileStorage.__file_path, "w") as f:
            json.dump(dict_to_json, f)

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
