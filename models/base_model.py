#!/usr/bin/python3
""" Class Basemodel that defines attributes/methods"""

import uuid
from datetime import datetime
import models

class BaseModel:
    """Class Basemodel"""

    def __init__(self, *args, **kwargs):
        """arguments for the constructor of a BaseModel"""
        format = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for key in kwargs:
                if key == "id":
                    self.id = kwargs[key]
                if key == "created_at":
                    self.created_at = datetime.strptime(kwargs[key], format)
                if key == "updated_at":
                    self.updated_at = datetime.strptime(kwargs[key], format)

                else:
                    self.id = str(uuid4())
                    self.created_at = datetime.now()
                    self.updated_at = datetime.now()
                    models.storage.new(self)


                    def __str__(self):
                        """should print instance"""
                        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

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
