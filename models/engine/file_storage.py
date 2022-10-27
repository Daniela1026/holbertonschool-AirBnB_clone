#!/usr/bin/python3
""" recreate a BaseModel store first object"""

import datetime
import json
import os

class FileStorage:
    """serializes instances to a JSON"""

     __file_path = "file.json"
     __objects = {}

     def __init__(self):
         """class constructor"""

     def parse(self, arg):
        'return the name class'
        nameclass = arg.split(sep=".")
        name = str(nameclass[0])
        return name

     def all(self):
         """returns the dictionary __objects"""
         return self.__objects

     def new(self, obj):
         """sets in __objects the obj"""
         key = "{}.{}".format(obj.__class__.__name__, obj.id)
         self.__objects[key] = obj

     def save(self):
         """serializes __objects to the JSON"""
         new_dic = {}
        if self.__file_path is not None:
            for key, obj in self.__objects.items():
                new_dic[key] = obj.to_dict()
            with open(self.__file_path, 'w', encoding="utf-8") as f:
                json.dump(new_dic, f)
        else:
            self.__file_path = "file.json"

     def reload(self):
         """deserializes the JSON file to __objects"""
         from models.base_model import BaseModel
         from models.user import User
         from models.state import State
         from models.city import City
         from models.amenity import Amenity
         from models.place import Place
         from models.review import Review
         list_className = {
                 "BaseModel": BaseModel, "User": User,
                 "State": State, "City": City,
                 "Amenity": Amenity, "Place": Place,
                 "Review": Review}
         new_dic = {}
         name_class = ""
         if os.path.exists(self.__file_path):
             with open(self.__file_path, 'r', encoding="utf-8") as file_json:
                 new_dic = json.load(file_json)
                 for key, obj in new_dic.items():
                     name_class = self.parse(key)
                     new_obj = list_className[name_class](**obj)
                     new_dic[key] = new_obj
                     self.__objects = new_dic
                 else:
                     pass
