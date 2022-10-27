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
                if key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime
                            (value, "%Y-%m-%dT%H:%M:%S.%f"))
                elif key == "__class__":
                    continue
                else:
                    setattr(self, key, value)
                else:
                    self.id = str(uuid.uuid4())
                    self.created_at = datetime.now()
                    self.updated_at = datetime.now()
                    models.storage.new(self)

                    def __str__(self):
                        """should print instance"""
                        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))

                        def save(self):
                            """updates the public instance attribute updated_at"""
                            self.updated_at = datetime.now()
                            models.storage.save()

                            def to_dict(self):
                                """returns a dictionary containing all keys/values"""
                                my_dict = self.__dict__.copy()
                                my_dict['created_at'] = self.created_at.isoformat()
                                my_dict['updated_at'] = self.updated_at.isoformat()
                                my_dict['__class__'] = self.__class__.__name__
                                return(my_dict)
