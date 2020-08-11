#!/usr/bin/env python3
'''
classes:
BaseModel: Defines behavior for other sub-classes
'''

from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    ''' BaseModel Class '''

    def __init__(self, *args, **kwargs):
        ''' Constructor method '''
        if (kwargs):
            for key, value in kwargs.items():
                if (key == '__class__'):
                    continue
                elif (key == 'updated_at' or key == 'created_at'):
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if 'id' not in kwargs.keys():
                    self.id = str(uuid4())
                if 'created_at' not in kwargs.keys():
                    self.created_at = datetime.now()
                if 'updated_at' not in kwargs.keys():
                    self.updated_at = datetime.now()
                setattr(self, key, value)

        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        '''Print the BaseModel atrributes.'''
        return('[' + type(self).__name__ + '] (' + str(self.id) +
               ') ' + str(self.__dict__))

    def save(self):
        ''' Update updated_at attr '''
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        ''' Return a dictonary with all key/values '''
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        return new_dict
