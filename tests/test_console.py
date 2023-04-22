#!/usr/bin/python3
"""Unittest for the console"""

import unittest
import os
import json
import pycodestyle
import io
from console import HBNBCommand
from models.engine.file_storage import FileStorage
from unittest.mock import patch
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

class TestCommand(unittest.TestCase):
    """Sets test foe console"""

    def setup(self):
        """Empties file json"""
        FileStorage._FIleStorage__objects = {}
        FileStorage().save()

