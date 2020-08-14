#!/usr/bin/python3
"""Test Amenity"""
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Test Amenity file"""

    def tearDown(self):
        ''' After tests, remove json file '''
        try:
            remove("file.json")
        except Exception:
            pass

    def test_class(self):
        """Test the class."""
        amenity1 = Amenity()
        self.assertTrue(hasattr(amenity1, "id"))
        self.assertTrue(hasattr(amenity1, "created_at"))
        self.assertTrue(hasattr(amenity1, "updated_at"))
        self.assertEqual(amenity1.__class__.__name__, "Amenity")

    def test_father(self):
        """Test the class - BaseModel """
        amenity1 = Amenity()
        self.assertTrue(issubclass(amenity1.__class__, BaseModel))

    def test_class_kwargs(self):
        """Test the class passing kwargs"""
        dictonary = {
            'id': '662a23b3-abc7-4f43-81dc-64c000001c00', 'score': 100}
        amenity1 = Amenity(**dictonary)
        self.assertTrue(hasattr(amenity1, "id"))
        self.assertEqual(amenity1.id, '662a23b3-abc7-4f43-81dc-64c000001c00')
        self.assertTrue(hasattr(amenity1, "score"))
        self.assertEqual(amenity1.score, 100)
        self.assertTrue(hasattr(amenity1, "created_at"))
        self.assertTrue(type(amenity1.updated_at), datetime)
        self.assertTrue(hasattr(amenity1, "updated_at"))
        self.assertTrue(type(amenity1.created_at), datetime)
        self.assertEqual(amenity1.__class__.__name__, "Amenity")

    def test_father_kwargs(self):
        """Test the class - BaseModel passing kwargs """
        dictonary = {'id': '662a23b3-abc7-4f43-81dc-64c000000c00'}
        amenity1 = Amenity(**dictonary)
        self.assertTrue(issubclass(amenity1.__class__, BaseModel))

    def test_amenity(self):
        """Test attributes of the class."""
        my_amenity = Amenity()
        my_amenity.name = "Wi-Fi"
        self.assertEqual(my_amenity.name, 'Wi-Fi')

    def test_type(self):
        """Test amenity value type."""
        amenity1 = Amenity()
        self.assertEqual(type(amenity1.name), str)
        self.assertNotEqual(type(amenity1.name), list)

    def test_attribute(self):
        """Test another attributes."""
        amenity1 = Amenity()
        self.assertTrue(hasattr(amenity1, "name"))
        self.assertFalse(hasattr(amenity1, "area"))
