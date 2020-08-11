#!/usr/bin/python3
"""Test Review"""
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    """Test Review file"""

    def tearDown(self):
        ''' After tests, remove json file '''
        try:
            remove("file.json")
        except Exception:
            pass

    def test_class(self):
        """Test the class."""
        review1 = Review()
        self.assertTrue(hasattr(review1, "id"))
        self.assertTrue(hasattr(review1, "created_at"))
        self.assertTrue(hasattr(review1, "updated_at"))
        self.assertEqual(review1.__class__.__name__, "Review")

    def test_father(self):
        """Test the class - BaseModel """
        review1 = Review()
        self.assertTrue(issubclass(review1.__class__, BaseModel))

    def test_class_kwargs(self):
        """Test the class passing kwargs"""
        dictonary = {
            'id': '662a23b3-abc7-4f43-81dc-64c000001c00', 'score': 100}
        review1 = Review(**dictonary)
        self.assertTrue(hasattr(review1, "id"))
        self.assertEqual(review1.id, '662a23b3-abc7-4f43-81dc-64c000001c00')
        self.assertTrue(hasattr(review1, "score"))
        self.assertEqual(review1.score, 100)
        self.assertTrue(hasattr(review1, "created_at"))
        self.assertTrue(type(review1.updated_at), datetime)
        self.assertTrue(hasattr(review1, "updated_at"))
        self.assertTrue(type(review1.created_at), datetime)
        self.assertEqual(review1.__class__.__name__, "Review")

    def test_father_kwargs(self):
        """Test the class - BaseModel passing kwargs """
        dictonary = {'id': '662a23b3-abc7-4f43-81dc-64c000000c00'}
        review1 = Review(**dictonary)
        self.assertTrue(issubclass(review1.__class__, BaseModel))

    def test_Review(self):
        """Test attributes of the class."""
        my_Review = Review()
        my_Review.name = "LA"
        self.assertEqual(my_Review.name, 'LA')

    def test_attribute(self):
        """Test attributes."""
        review1 = Review()
        self.assertTrue(hasattr(review1, "updated_at"))
        self.assertTrue(hasattr(review1, "created_at"))
        self.assertTrue(hasattr(review1, "id"))
        self.assertEqual(type(review1.updated_at), datetime)
        self.assertEqual(type(review1.created_at), datetime)
        self.assertEqual(type(review1.id), str)
        self.assertFalse(hasattr(review1, "brent"))
        self.assertTrue(hasattr(review1, "place_id"))
        self.assertTrue(hasattr(review1, "user_id"))
        self.assertTrue(hasattr(review1, "text"))
        self.assertEqual(type(review1.text), str)
