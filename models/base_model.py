#!/usr/bin/python3
""" Class Basemodel that defines attributes/methods"""

import uuid
from datetime import datetime
import models

class BaseModel:
    """Class Basemodel"""

    def __init__(self, *args, **kwargs):
        """arguments for the constructor of a BaseModel"""
        if kwargs:
            for key, value in kwargs.items():
                if key in ('created_at', 'updated_at'):
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')

                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.updated_at = self.created_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """prints string representation of base"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """saves"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """dictionary"""
        BaseDict = self.__dict__.copy()
        BaseDict["__class__"] = self.__class__.__name__
        BaseDict["created_at"] = self.created_at.isoformat()
        BaseDict["updated_at"] = self.updated_at.isoformat()
        return BaseDict
