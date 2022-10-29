#!/usr/bin/python3

"""
Contains the FileStorage class
"""

import json
from os import path


class FileStorage:
    """
    File Storage class
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Return content of __objects attribute"""
        return self.__objects

    def new(self, obj):
        """ Sets in __objects the obj with key <obj class name>.id"""
        key = f"{obj.__class__.__name__}.{ obj.id}"
        self.__objects[key] = obj

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path)"""
        dict_json = {}
        for key, value in self.__objects.items():
            dict_json[key] = value.to_dict()
        with open(self.__file_path, "w", encoding="utf-8") as file:
            file.write(json.dumps(dict_json))

    def reload(self):
        """  Deserializes the JSON file to __objects """
        from models.base_model import BaseModel
        from models.user import User
        from models.amenity import Amenity
        from models.city import City
        from models.place import Place
        from models.state import State
        from models.review import Review

        if path.exists(self.__file_path):
            with open(self.__file_path, "r", encoding="utf-8") as file:
                json_object = json.loads(file.read())

            for key, value in json_object.items():
                self.__objects[key] = eval(value['__class__'])(**value)
