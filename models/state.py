#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    if getenv('HBNB_STORAGE_TYPE') == 'db':
        __tablename__ = 'states'
        """ State class """
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
