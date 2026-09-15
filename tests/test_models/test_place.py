#!/usr/bin/python3
"""Unittests for Place class."""
import unittest
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """Test suite for Place class."""

    def test_inheritance(self):
        """Test Place inherits from BaseModel."""
        p = Place()
        self.assertIsInstance(p, BaseModel)

    def test_attributes(self):
        """Test Place default attribute values."""
        p = Place()
        self.assertEqual(p.city_id, "")
        self.assertEqual(p.user_id, "")
        self.assertEqual(p.name, "")
        self.assertEqual(p.description, "")
        self.assertEqual(p.number_rooms, 0)
        self.assertEqual(p.number_bathrooms, 0)
        self.assertEqual(p.max_guest, 0)
        self.assertEqual(p.price_by_night, 0)
        self.assertEqual(p.latitude, 0.0)
        self.assertEqual(p.longitude, 0.0)
        self.assertEqual(p.amenity_ids, [])


if __name__ == "__main__":
    unittest.main()
