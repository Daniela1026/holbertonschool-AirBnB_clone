#!/usr/bin/python3
"""
This module is meant to define the storage class
"""
import json
import os.path

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
        key = str(obj.__class__.__name__) + "." + str(obj.id)
        value_dict = obj
        FileStorage.__objects[key] = value_dict

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)
        """
        new_dict = {}
        for key in self.__objects.keys():
            new_dict[key] = self.__objects[key].to_dict()
        with open(self.__file_path, "w") as f:
            f.write(json.dumps(new_dict))

    def reload(self):
        """Deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists ; otherwise, do nothing. If the file doesn’t
        exist, no exception should be raised)
        """
        from models.base_model import BaseModel
        from models.engine.file_storage import FileStorage
        from models.user import User
        from models.amenity import Amenity
        from models.city import City
        from models.place import Place
        from models.state import State
        from models.review import Review

        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r") as f:
                aux = json.loads(f.read())
                for key, val in aux.items():
                    self.__objects[key] = eval(val["__class__"])(**val)
