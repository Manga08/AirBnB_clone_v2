#!/usr/bin/python3
"""Test Place"""
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.place import Place


class TestPlace(unittest.TestCase):
    """Test Place file"""

    def tearDown(self):
        ''' After tests, remove json file '''
        try:
            remove("file.json")
        except Exception:
            pass

    def test_class(self):
        """Test the class."""
        place1 = Place()
        self.assertTrue(hasattr(place1, "id"))
        self.assertTrue(hasattr(place1, "created_at"))
        self.assertTrue(hasattr(place1, "updated_at"))
        self.assertEqual(place1.__class__.__name__, "Place")

    def test_father(self):
        """Test the class - BaseModel """
        place1 = Place()
        self.assertTrue(issubclass(place1.__class__, BaseModel))

    def test_class_kwargs(self):
        """Test the class passing kwargs"""
        dictonary = {
            'id': '662a23b3-abc7-4f43-81dc-64c000001c00', 'score': 100}
        place1 = Place(**dictonary)
        self.assertTrue(hasattr(place1, "id"))
        self.assertEqual(place1.id, '662a23b3-abc7-4f43-81dc-64c000001c00')
        self.assertTrue(hasattr(place1, "score"))
        self.assertEqual(place1.score, 100)
        self.assertTrue(hasattr(place1, "created_at"))
        self.assertTrue(type(place1.updated_at), datetime)
        self.assertTrue(hasattr(place1, "updated_at"))
        self.assertTrue(type(place1.created_at), datetime)
        self.assertEqual(place1.__class__.__name__, "Place")

    def test_father_kwargs(self):
        """Test the class - BaseModel passing kwargs """
        dictonary = {'id': '662a23b3-abc7-4f43-81dc-64c000000c00'}
        place1 = Place(**dictonary)
        self.assertTrue(issubclass(place1.__class__, BaseModel))

    def test_Place(self):
        """Test attributes of the class."""
        my_Place = Place()
        my_Place.name = "LA"
        self.assertEqual(my_Place.name, 'LA')

    def test_type(self):
        """Test Place value type."""
        place1 = Place()
        self.assertEqual(type(place1.name), str)
        self.assertNotEqual(type(place1.name), list)

    def test_attribute(self):
        """Test attributes."""
        place1 = Place()
        self.assertTrue(hasattr(place1, "updated_at"))
        self.assertTrue(hasattr(place1, "created_at"))
        self.assertTrue(hasattr(place1, "id"))
        self.assertTrue(hasattr(place1, "name"))
        self.assertEqual(type(place1.updated_at), datetime)
        self.assertEqual(type(place1.created_at), datetime)
        self.assertEqual(type(place1.id), str)
        self.assertEqual(type(place1.name), str)
        self.assertFalse(hasattr(place1, "brent"))
        self.assertTrue(hasattr(place1, "city_id"))
        self.assertEqual(type(place1.city_id), str)
        self.assertTrue(hasattr(place1, "user_id"))
        self.assertEqual(type(place1.user_id), str)
        self.assertTrue(hasattr(place1, "description"))
        self.assertEqual(type(place1.description), str)
        self.assertTrue(hasattr(place1, "number_rooms"))
        self.assertEqual(type(place1.number_rooms), int)
        self.assertTrue(hasattr(place1, "number_bathrooms"))
        self.assertEqual(type(place1.number_bathrooms), int)
        self.assertTrue(hasattr(place1, "max_guest"))
        self.assertEqual(type(place1.max_guest), int)
        self.assertTrue(hasattr(place1, "price_by_night"))
        self.assertEqual(type(place1.price_by_night), int)
        self.assertTrue(hasattr(place1, "latitude"))
        self.assertEqual(type(place1.latitude), float)
        self.assertTrue(hasattr(place1, "longitude"))
        self.assertEqual(type(place1.longitude), float)
        self.assertTrue(hasattr(place1, "amenity_ids"))
        self.assertEqual(type(place1.amenity_ids), list)
