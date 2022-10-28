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
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)
        """
        aux_dict = {key: value.to_dict() for key, value in self.all().items()}

        with open(FileStorage.__file_path, mode="w+", encoding="utf-8") as f:
            f.write(json.dumps(aux_dict))

    def reload(self):
        """Deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists ; otherwise, do nothing. If the file doesn’t
        exist, no exception should be raised)
        """
        from models.base_model import BaseModel
        from models.user import User
        from models.amenity import Amenity
        from models.city import City
        from models.place import Place
        from models.state import State
        from models.review import Review

        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                str_read = f.read()

            python_obj = json.loads(str_read)
            FileStorage.__objects = {k: eval(f"{v['__class__']}(**{v})")
                                     for k, v in python_obj.items()}
