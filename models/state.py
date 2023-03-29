#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """state class"""
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='state', cascade='delete')
    else:
        name = ''

    @property
    def cities(self):
        """7"""
        import models
        citlist = []
        for city in models.storage.all('City').values():
            if city.state_id == self.id:
                citlist.append(city)
        return citlist
