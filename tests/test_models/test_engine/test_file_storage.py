#!/usr/bin/python3
"""Unittests for FileStorage class."""
import unittest
import os
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class TestFileStorage(unittest.TestCase):
    """Test suite for FileStorage class."""

    def setUp(self):
        """Clean up before test."""
        if os.path.exists("file.json"):
            os.remove("file.json")

    def tearDown(self):
        """Clean up after test."""
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_all_returns_dict(self):
        """Test all method returns dictionary."""
        self.assertIsInstance(storage.all(), dict)

    def test_new_and_save(self):
        """Test new and save methods."""
        bm = BaseModel()
        u = User()
        storage.new(bm)
        storage.new(u)
        storage.save()
        self.assertTrue(os.path.exists("file.json"))
        with open("file.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        self.assertIn("BaseModel.{}".format(bm.id), data)
        self.assertIn("User.{}".format(u.id), data)

    def test_reload(self):
        """Test reload method."""
        bm = BaseModel()
        bm.save()
        storage.reload()
        all_objs = storage.all()
        self.assertIn("BaseModel.{}".format(bm.id), all_objs)


if __name__ == "__main__":
    unittest.main()
