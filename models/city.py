#!/usr/bin/python3
""" City Module for HBNB project """
<<<<<<< HEAD
from models.base_model import BaseModel, Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, Column, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from models.place import Place

class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = "cities"

    state_id = Column(String(60), nullable=False, foreign_key(states.id))
    name = Column(String(128), nullable=False)
    places = relationship("Place", cascade='all, delete, delete-orphan', backref="cities")
=======
from base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String, ForeignKey


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = cities
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), nullable=False, ForeignKey=('states.id'))
    else:
        name = ""
        state_id = ""
>>>>>>> 16cd3379872178456912f305a058ba7fa62d62b9
