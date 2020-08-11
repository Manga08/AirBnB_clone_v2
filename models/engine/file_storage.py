#!/usr/bin/env python3
'''
classes:
FileStorage: serialize/deserialize objects to JSON
'''
import json
import os
import uuid
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    ''' FileStorage engine class '''
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        '''Returns the dictionary __objects'''

        print_dict = {}
        for key, value in FileStorage.__objects.items():
            if isinstance(value, cls):
                print_dict[key] = value
        if cls is not None and len(print_dict) > 1:
            return print_dict
        return FileStorage.__objects

    def new(self, obj):
        ''' sets in __objects the obj with key <obj class name>.id '''
        FileStorage.__objects[obj.__class__.__name__ + '.' + str(obj.id)] = obj

    def save(self):
        ''' serializes __objects to the JSON file (path: __file_path) '''
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as file:
            new_dict = {key: obj.to_dict() for key, obj in
                        FileStorage.__objects.items()}
            json.dump(new_dict, file)

    def reload(self):
        '''Deserializes the JSON file to __objects.'''
        try:
            if (os.path.isfile(FileStorage.__file_path)):
                with open(FileStorage.__file_path, 'r', encoding='utf-8') as file:
                    objs = json.load(file)
                    for key, value in objs.items():
                        FileStorage.__objects[key] = eval(
                            value['__class__'])(**value)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        '''Delete obj from __objects if it’s inside.'''
        try:
            if obj:
                formats = "{}.{}".format(type(obj).__name__, obj.id)
                del FileStorage.__objects[formats]
        except:
            pass
