#!/usr/bin/python3
"""Unittests for Review class."""
import unittest
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """Test suite for Review class."""

    def test_inheritance(self):
        """Test Review inherits from BaseModel."""
        r = Review()
        self.assertIsInstance(r, BaseModel)

    def test_attributes(self):
        """Test Review default attribute values."""
        r = Review()
        self.assertEqual(r.place_id, "")
        self.assertEqual(r.user_id, "")
        self.assertEqual(r.text, "")


if __name__ == "__main__":
    unittest.main()
