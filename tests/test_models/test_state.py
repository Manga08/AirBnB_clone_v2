#!/usr/bin/python3
"""Test State"""
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    """Test State file"""

    def tearDown(self):
        ''' After tests, remove json file '''
        try:
            remove("file.json")
        except Exception:
            pass

    def test_class(self):
        """Test the class."""
        state1 = State()
        self.assertTrue(hasattr(state1, "id"))
        self.assertTrue(hasattr(state1, "created_at"))
        self.assertTrue(hasattr(state1, "updated_at"))
        self.assertEqual(state1.__class__.__name__, "State")

    def test_father(self):
        """Test the class - BaseModel """
        state1 = State()
        self.assertTrue(issubclass(state1.__class__, BaseModel))

    def test_class_kwargs(self):
        """Test the class passing kwargs"""
        dictonary = {
            'id': '662a23b3-abc7-4f43-81dc-64c000001c00', 'score': 100}
        state1 = State(**dictonary)
        self.assertTrue(hasattr(state1, "id"))
        self.assertEqual(state1.id, '662a23b3-abc7-4f43-81dc-64c000001c00')
        self.assertTrue(hasattr(state1, "score"))
        self.assertEqual(state1.score, 100)
        self.assertTrue(hasattr(state1, "created_at"))
        self.assertTrue(type(state1.updated_at), datetime)
        self.assertTrue(hasattr(state1, "updated_at"))
        self.assertTrue(type(state1.created_at), datetime)
        self.assertEqual(state1.__class__.__name__, "State")

    def test_father_kwargs(self):
        """Test the class - BaseModel passing kwargs """
        dictonary = {'id': '662a23b3-abc7-4f43-81dc-64c000000c00'}
        state1 = State(**dictonary)
        self.assertTrue(issubclass(state1.__class__, BaseModel))

    def test_State(self):
        """Test attributes of the class."""
        my_State = State()
        my_State.name = "LA"
        self.assertEqual(my_State.name, 'LA')

    def test_attribute(self):
        """Test another attributes."""
        state1 = State()
        self.assertTrue(hasattr(state1, "name"))
        self.assertFalse(hasattr(state1, "area"))
