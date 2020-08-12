#!/usr/bin/python3
"""Test City"""
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    """Test City file"""

    def tearDown(self):
        ''' After tests, remove json file '''
        try:
            remove("file.json")
        except Exception:
            pass

    def test_class(self):
        """Test the class."""
        city1 = City()
        self.assertTrue(hasattr(city1, "id"))
        self.assertTrue(hasattr(city1, "created_at"))
        self.assertTrue(hasattr(city1, "updated_at"))
        self.assertEqual(city1.__class__.__name__, "City")

    def test_father(self):
        """Test the class - BaseModel """
        city1 = City()
        self.assertTrue(issubclass(city1.__class__, BaseModel))

    def test_class_kwargs(self):
        """Test the class passing kwargs"""
        dictonary = {
            'id': '662a23b3-abc7-4f43-81dc-64c000001c00', 'name': 'New York'}
        city1 = City(**dictonary)
        self.assertTrue(hasattr(city1, "id"))
        self.assertEqual(city1.id, '662a23b3-abc7-4f43-81dc-64c000001c00')
        self.assertTrue(hasattr(city1, "name"))
        self.assertEqual(city1.name, 'New York')
        self.assertTrue(hasattr(city1, "created_at"))
        self.assertTrue(type(city1.updated_at), datetime)
        self.assertTrue(hasattr(city1, "updated_at"))
        self.assertTrue(type(city1.created_at), datetime)
        self.assertEqual(city1.__class__.__name__, "City")

    def test_father_kwargs(self):
        """Test the class - BaseModel passing kwargs """
        dictonary = {'id': '662a23b3-abc7-4f43-81dc-64c000000c00'}
        city1 = City(**dictonary)
        self.assertTrue(issubclass(city1.__class__, BaseModel))

    def test_City(self):
        """Test attributes of the class."""
        my_City = City()
        my_City.name = "Bogota"
        my_City.state_id = "571"
        self.assertEqual(my_City.name, 'Bogota')
        self.assertEqual(my_City.state_id, '571')

    def test_attribute(self):
        """Test another attributes."""
        city1 = City()
        self.assertTrue(hasattr(city1, "name"))
        self.assertFalse(hasattr(city1, "area"))
