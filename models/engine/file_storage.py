#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
import models
from models import city, place, review, state, amenity, user, base_model


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    CDIC = {
        'City': city.City,
        'Place': place.Place,
        'Review': review.Review,
        'State': state.State,
        'Amenity': amenity.Amenity,
        'User': user.User
    }
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls is not None:
            if cls in self.CDIC.keys():
                cls = self.CDIC.get(cls)
            spec_rich = {}
            for ky, vl in self.__objects.items():
                if cls == type(vl):
                    spec_rich[ky] = vl
            return spec_rich
        return self.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
                if '_sa_instance_state' in temp:
                    del temp['_sa_instance_state']
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

    def delete(self, obj=None):
        """deletes objects"""
        if obj is None:
            return
        else:
            ob = ("{}.{}").format(obj.__class__.__name__, obj.id)
            if ob in self.__objects:
                del self.__objects[ob]
                self.save()

    def close(self):
        self.reload()
