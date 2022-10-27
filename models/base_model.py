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
            models.storage.new(self)

    def __str__(self):
        """
        Representation and format used
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)

    def save(self):
        """
        Updates all info into the storage
        """
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """
        Dictionary containing all keys/values of __dict__ of the instance
        """
        d = self.__dict__.copy()
        d["__class__"] = self.__class__.__name__
        d["created_at"] = d["created_at"].isoformat("T")
        d["updated_at"] = d["updated_at"].isoformat("T")
        return d
