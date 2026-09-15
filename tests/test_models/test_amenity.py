#!/usr/bin/python3
"""Unittests for Amenity class."""
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """Test suite for Amenity class."""

    def test_inheritance(self):
        """Test Amenity inherits from BaseModel."""
        a = Amenity()
        self.assertIsInstance(a, BaseModel)

    def test_attributes(self):
        """Test Amenity default attribute values."""
        a = Amenity()
        self.assertTrue(hasattr(a, "name"))
        self.assertEqual(a.name, "")


if __name__ == "__main__":
    unittest.main()
