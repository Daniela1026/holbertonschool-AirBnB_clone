#!/usr/bin/python3
"""
This module will define all common attributes/methods for other classes
"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """
    Base class for all common attributes/methods for other classes
    """
    def __init__(self, *args, **kwargs):
        """
        initialize class BaseModel
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key == 'created_at' or key == 'update_at':
                    value = datetime.fromisoformat(value)
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """
        Representation and format used
        """
        cls_name = self.__class__.__name__
        msg_format = "[{}] ({}) {}"
        return msg_format.format(cls_name, self.id, self.__dict__)

    def save(self):
        """
        Updates all info into the storage
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Dictionary containing all keys/values of __dict__ of the instance
        """
        dict_return = self.__dict__.copy()
        dict_return["__class__"] = self.__class__.__name__
        dict_return["created_at"] = self.created_at.isoformat()
        dict_return["updated_at"] = self.updated_at.isoformat()

        return dict_return
