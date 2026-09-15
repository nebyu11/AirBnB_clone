#!/usr/bin/python3
"""Unittests for State class."""
import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """Test suite for State class."""

    def test_inheritance(self):
        """Test State inherits from BaseModel."""
        s = State()
        self.assertIsInstance(s, BaseModel)

    def test_attributes(self):
        """Test State default attribute values."""
        s = State()
        self.assertTrue(hasattr(s, "name"))
        self.assertEqual(s.name, "")


if __name__ == "__main__":
    unittest.main()
