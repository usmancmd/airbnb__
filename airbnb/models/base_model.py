#!/usr/bin/env python3

"""Defines BaseModel class that defines all common attributes and methods"""

import uuid
from datetime import datetime
import models


class BaseModel:
    """BaseModel class defines all common attributes and methods"""

    def __init__(self, *args, **kwargs):
        """initialize a new BaseModel class

        Args:
            *args (any type): unused
            **kargs (dict): key/value pairs of attribute
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

#        time_format = "%Y-%m-%dT%H:%M:%S.%"
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.fromisoformat(value)
                else:
                    self.__dict__[key] = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Return string represention of BaseModel instance"""
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        """Updates the public instance attribute"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary
            containing all keys/values with current datetime"""

        copy_dict = self.__dict__.copy()
        copy_dict["created_at"] = self.created_at.isoformat()
        copy_dict["updated_at"] = self.updated_at.isoformat()
        copy_dict["__class__"] = self.__class__.__name__
        return copy_dict
