#!/usr/bin/python3
""" holds class User"""
import hashlib
import models
from models.base_model import BaseModel, Base
from models.review import Review
from os import getenv
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
from models.place import Place
from models.review import Review

class User(BaseModel, Base):
    """user class model"""
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    _password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    places = relationship("Place", cascade='all, delete, delete-orphan', backref="user")
    reviews = relationship("Review", cascade='all, delete, delete-orphan', backref="user")

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, pwd):
        """ hasing password vallues """
        self._password = pwd
