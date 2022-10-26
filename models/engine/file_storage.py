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

     def all(self):
         """returns the dictionary __objects"""
         return FileStorage.__objects

     def new(self, obj):
         """sets in __objects the obj"""
         key = "{}.{}".format(type(obj).__name__, obj.id)
         FileStorage.__objects[key] = obj

     def save(self):
         """serializes __objects to the JSON"""
         jsonObject = {}
        for key in self.__objects:
            jsonObject[key] = self.__objects[key].to_dict()
        with open(self.__file_path, "w", encoding='utf-8') as f:
            json.dump(jsonObject, f)

     def reload(self):
         try:
            with open(self.__file_path, 'r') as f:
                value = json.load(f)
            for key in value:
                self.__objects[key] = classes[value[key]["__class__"]](**value[key])
        except FileNotFoundError:
            pass
