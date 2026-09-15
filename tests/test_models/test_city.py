#!/usr/bin/python3
"""Unittests for City class."""
import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """Test suite for City class."""

    def test_inheritance(self):
        """Test City inherits from BaseModel."""
        c = City()
        self.assertIsInstance(c, BaseModel)

    def test_attributes(self):
        """Test City default attribute values."""
        c = City()
        self.assertTrue(hasattr(c, "state_id"))
        self.assertTrue(hasattr(c, "name"))
        self.assertEqual(c.state_id, "")
        self.assertEqual(c.name, "")


if __name__ == "__main__":
    unittest.main()
