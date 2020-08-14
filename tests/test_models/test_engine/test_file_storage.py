#!/usr/bin/env python3
'''
test: FileStorage
'''

import unittest
from os import path
from models import storage
from models.user import User
from models.city import City
from models.state import State
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class test_file_storage(unittest.TestCase):
    ''' Unittest for file_storage.py file'''

    def setUp(self):
        ''' Start all test with empty storage '''
        try:
            remove('file.json')
        except Exception:
            pass
        FileStorage._FileStorage__objects = {}

    def tearDown(self):
        ''' Remove file.json after tests '''
        try:
            remove('file.json')
        except Exception:
            pass

    def test_no_objs(self):
        ''' empty storage '''
        self.assertEqual(storage.all(), {})


    def test_new_empty(self):
        ''' test for new method (error)'''
        with self.assertRaises(TypeError):
            storage.new()

    def test_new_classes(self):
        ''' test for new method (valid) '''
        obj = BaseModel(id='123')
        obj_key = 'BaseModel' + '.' + obj.id
        obj1 = User(id='01')
        obj1_key = 'User' + '.' + obj1.id
        obj2 = City(id='02')
        obj2_key = 'City' + '.' + obj2.id
        obj3 = Amenity(id='03')
        obj3_key = 'Amenity' + '.' + obj3.id
        obj4 = Place(id='04')
        obj4_key = 'Place' + '.' + obj4.id
        obj5 = Review(id='05')
        obj5_key = 'Review' + '.' + obj5.id
        obj6 = State(id='06')
        obj6_key = 'State' + '.' + obj6.id

        self.assertEqual(storage.all(), {})
        obj.id = 123
        storage.new(obj)
        storage.new(obj1)
        storage.new(obj2)
        storage.new(obj3)
        storage.new(obj4)
        storage.new(obj5)
        storage.new(obj6)
        self.assertEqual(obj, storage.all()[obj_key])
        self.assertEqual(obj1, storage.all()[obj1_key])
        self.assertEqual(obj2, storage.all()[obj2_key])
        self.assertEqual(obj3, storage.all()[obj3_key])
        self.assertEqual(obj4, storage.all()[obj4_key])
        self.assertEqual(obj5, storage.all()[obj5_key])
        self.assertEqual(obj6, storage.all()[obj6_key])
