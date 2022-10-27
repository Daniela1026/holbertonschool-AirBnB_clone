#!/usr/bin/python3
""" recreate a BaseModel store first object"""

import json
import os
from models.base_model import BaseModel

class FileStorage():
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        FileStorage.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def destroy(self, id):
        del FileStorage.__objects[id]
        self.save()

    def save(self):
        """
        The above function saves the objects in the FileStorage class \
            to a JSON file.
        """
        objs = {}
        for id in FileStorage.__objects:
            objs[id] = FileStorage.__objects[id].to_dict()
        with open(FileStorage.__file_path, 'w') as f:
            f.seek(0)
            f.write(json.dumps(objs))
            f.truncate()

    def reload(self):
        """
        This function reloads the data from the json file
        """
        FileStorage.__objects.clear()
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as f:
                file_content = f.read()
                data = json.loads(file_content) \
                    if file_content is not None else []
                for key, value in data.items():
                    FileStorage.__objects[key] = \
                        globals()[value['__class__']](**valu)
