#!/usr/bin/python3
"""Unittests for User class."""
import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """Test suite for User class."""

    def test_inheritance(self):
        """Test User inherits from BaseModel."""
        u = User()
        self.assertIsInstance(u, BaseModel)

    def test_attributes(self):
        """Test User default attribute values."""
        u = User()
        self.assertTrue(hasattr(u, "email"))
        self.assertTrue(hasattr(u, "password"))
        self.assertTrue(hasattr(u, "first_name"))
        self.assertTrue(hasattr(u, "last_name"))
        self.assertEqual(u.email, "")
        self.assertEqual(u.password, "")
        self.assertEqual(u.first_name, "")
        self.assertEqual(u.last_name, "")


if __name__ == "__main__":
    unittest.main()
