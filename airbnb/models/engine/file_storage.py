#!/usr/bin/python3
"""
Defines FileStorage class that serializes instances to a JSON file
and deserializes JSON file to instances
"""

import json
from models.base_model import BaseModel
import os


class FileStorage:
    """FileStorage class that serializes instances to a JSON file

        Attributes:
            __file_path(string): path to the JSON file
            __objects(dict): empty but will store all objects
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        obname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(obname, obj.id)] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""

        with open(FileStorage.__file_path, mode="w") as f:
            obj_to_dict = {}
            for key, value in FileStorage.__objects.items():
                obj_to_dict[key] = value.to_dict()
            json.dump(obj_to_dict, f)

    def reload(self):
        """
        Deserializes the JSON file to __objects
        only if the JSON file (__file_path) exists ;
        otherwise, do nothing.
        """
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, mode="r") as f:
                FileStorage.__objects = json.load(f)
