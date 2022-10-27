#!/usr/bin/python3
""" recreate a BaseModel store first object"""

from models.base_model import BaseModel
from models.user import User
import json
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

cla_i = {"BaseModel": BaseModel, "User": User, "Review": Review,
         "Amenity": Amenity, "City": City, "State": State, "Place": Place}


class FileStorage:
    """serializes instances to a JSON file and
    deserializes JSON file to instances"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        dic = {}
        for key in self.__objects.keys():
            dic[key] = self.__objects[key].to_dict()
        with open(self.__file_path, "w") as f:
            json.dump(dic, f)

    def reload(self):
        """deserializes the JSON file to __objects
        (only if the JSON file (__file_path)"""
        try:
            with open(self.__file_path, "r") as f:
                jr = json.load(f)
            for key in jr:
                self.__objects[key] = cla_i[jr[key]["__class__"]](**jr[key])
        except Exception:
            pass
