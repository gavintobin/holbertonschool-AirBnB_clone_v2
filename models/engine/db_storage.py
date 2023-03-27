#!/usr/bin/python3
from models.base_model import Base, BaseModel
from sqlalchemy import create_engine
from sqlalchemy.orm import session, sessionmaker, scoped_session
from os import getenv
from models import city, place, review, state, amenity, user


class DBStorage:
    __engine = None
    __session = None
    CDIC = {
        'City': city.City,
        'Place': place.Place,
        'Review': review.Review,
        'State': state.State,
        'Amenity': amenity.Amenity,
        'User': user.User
    }

    def __init__(self):
        from models.base_model import Base, BaseModel
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(getenv('HBNB_MYSQL_USER'),
                                              getenv('HBNB_MYSQL_PWD'),
                                              getenv('HBNB_MYSQL_HOST'),
                                              getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.dropall(self.__engine)

    def all(self, cls=None):
        obj_dct = {}
        qry = []
        if cls is None:
            for cls_typ in DBStorage.CDIC.values():
                qry.extend(self.__session.query(cls_typ).all())
        else:
            if cls in self.CDIC.keys():
                cls = self.CDIC.get(cls)
            qry = self.__session.query(cls)
        for obj in qry:
            obj_key = "{}.{}".format(type(obj).__name__, obj.id)
            obj_dct[obj_key] = obj
        return obj_dct

    def add(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        Base.metadata.create_all(self.__engine)
        sesh = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sesh)
        self.__session = Session()

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.__session.add(obj)

    def close(self):
        self.__session.close()
