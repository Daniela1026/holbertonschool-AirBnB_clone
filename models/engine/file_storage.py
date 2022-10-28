#!/usr/bin/python3
"""
This module is meant to define the storage class
"""
from models.base_model import BaseModel
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
        return FileStorage.__objects

    def new(self, obj):
        """Creates a new objects"""
        key = obj.__class__.__name__ + '.' + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """Saves the objects to JSON"""
        new_dict = {}
        for i in self.__objects:
            new_dict[i] = self.__objects[i].to_dict()
        with open(FileStorage.__file_path, 'w') as f:
            f.write(json.dumps(new_dict, default=str))

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

        classes_dict = {'BaseModel': BaseModel, 'Amenity': Amenity,
                        'City': City, 'Place': Place, 'Review': Review,
                        'User': User, 'State': State}
        try:
            with open(FileStorage.__file_path, 'r') as f:
                for i, j in json.load(f).items():
                    splitted = str(i).split('.')
                    if splitted[0] in classes_dict.keys():
                        self.__objects[i] = classes_dict[splitted[0]](**j)
        except:
            pass
