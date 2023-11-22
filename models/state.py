#!/usr/bin/python3
""" State Module for HBNB project """

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import os


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)

        cities = relationship(
            "City", backref="state", cascade="all, delete-orphan")
    else:
        name = ""

        @property
        @property
        def cities(self):
            from models import storage
            all_cities = storage.all(storage.classes['City'])
            return [city for city in all_cities.values() if getattr(city, 'state_id') == self.id]

