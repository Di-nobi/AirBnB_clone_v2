#!/usr/bin/python3
"""Module that checks state.py """
from tests.test_models.test_base_model import test_basemodel
from models.state import State


class test_state(test_basemodel):
    """Class test """

    def __init__(self, *args, **kwargs):
        """Constructor """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """Testing of state 3 """
        new = self.value()
        self.assertEqual(type(new.name), str)
