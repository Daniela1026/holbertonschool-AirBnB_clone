#!/usr/bin/python3
"""
This module will define all common attributes/methods for other classes
"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """ Base class for all common attributes/methods for other classes"""
    def __init__(self, *args, **kwargs):
        """ Method __init__ initialize the all attibutes """
      if len(kwargs) > 0:
            kwargs["created_at"] = datetime.strptime(kwargs["created_at"],
                                                     "%Y-%m-%dT%H:%M:%S.%f")
            kwargs["updated_at"] = datetime.strptime(kwargs["updated_at"],
                                                     "%Y-%m-%dT%H:%M:%S.%f")
            for k, v in kwargs.items():
                if k == "__class__":
                    continue
                else:
                    setattr(self, k, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.today()
            self.updated_at = self.created_at

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
        self.updated_at = datetime.today()

    def to_dict(self):
        """
        Dictionary containing all keys/values of __dict__ of the instance
        """
        dict_return = self.__dict__.copy()
        dict_return["__class__"] = self.__class__.__name__
        dict_return["created_at"] = self.created_at.isoformat()
        dict_return["updated_at"] = self.updated_at.isoformat()

        return dict_return
