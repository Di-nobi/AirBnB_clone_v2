#!/usr/bin/python3
"""Test for place """
from tests.test_models.test_base_model import test_basemodel
from models.place import Place


class test_Place(test_basemodel):
    """Test class """

    def __init__(self, *args, **kwargs):
        """Constructor for place """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """Tests the city id """
        new = self.value()
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """Test for user id """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """Test for user name """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """Test for description """
        new = self.value()
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """Tests the number of rooms """
        new = self.value()
        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """Tests number of bathrooms """
        new = self.value()
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """Checks for the maximum number of guests """
        new = self.value()
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """ Price at night"""
        new = self.value()
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """Tests latitude """
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """Tests longitude """
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_amenity_ids(self):
        """ Tests the amenity id"""
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)
