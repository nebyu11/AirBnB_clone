#!/usr/bin/python3
"""Unittests for console.py (HBNBCommand)."""
import unittest
from io import StringIO
import sys
import os
from console import HBNBCommand
from models import storage


class TestHBNBCommand(unittest.TestCase):
    """Test suite for HBNBCommand console."""

    def setUp(self):
        """Redirect stdout."""
        self.held_output = StringIO()
        sys.stdout = self.held_output

    def tearDown(self):
        """Restore stdout."""
        sys.stdout = sys.__stdout__
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_quit(self):
        """Test quit command."""
        cmd = HBNBCommand()
        self.assertTrue(cmd.onecmd("quit"))

    def test_EOF(self):
        """Test EOF command."""
        cmd = HBNBCommand()
        self.assertTrue(cmd.onecmd("EOF"))

    def test_create_missing_class(self):
        """Test create without class name."""
        cmd = HBNBCommand()
        cmd.onecmd("create")
        self.assertIn("** class name missing **", self.held_output.getvalue())

    def test_create_invalid_class(self):
        """Test create with invalid class name."""
        cmd = HBNBCommand()
        cmd.onecmd("create InvalidClass")
        self.assertIn("** class doesn't exist **", self.held_output.getvalue())

    def test_create_valid(self):
        """Test create with valid class."""
        cmd = HBNBCommand()
        cmd.onecmd("create BaseModel")
        obj_id = self.held_output.getvalue().strip()
        self.assertIn("BaseModel.{}".format(obj_id), storage.all())

    def test_show_missing_class(self):
        """Test show without class name."""
        cmd = HBNBCommand()
        cmd.onecmd("show")
        self.assertIn("** class name missing **", self.held_output.getvalue())

    def test_show_missing_id(self):
        """Test show without id."""
        cmd = HBNBCommand()
        cmd.onecmd("show BaseModel")
        self.assertIn("** instance id missing **", self.held_output.getvalue())

    def test_show_no_instance(self):
        """Test show with non-existent id."""
        cmd = HBNBCommand()
        cmd.onecmd("show BaseModel 999999")
        self.assertIn("** no instance found **", self.held_output.getvalue())

    def test_all(self):
        """Test all command."""
        cmd = HBNBCommand()
        cmd.onecmd("create User")
        self.held_output.truncate(0)
        self.held_output.seek(0)
        cmd.onecmd("all User")
        self.assertIn("[User]", self.held_output.getvalue())

    def test_update(self):
        """Test update command."""
        cmd = HBNBCommand()
        cmd.onecmd("create User")
        user_id = self.held_output.getvalue().strip()
        self.held_output.truncate(0)
        self.held_output.seek(0)
        cmd.onecmd('update User {} first_name "Betty"'.format(user_id))
        cmd.onecmd("show User {}".format(user_id))
        self.assertIn("'first_name': 'Betty'", self.held_output.getvalue())


if __name__ == "__main__":
    unittest.main()
