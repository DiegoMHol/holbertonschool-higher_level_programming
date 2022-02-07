#!/usr/bin/python3
""" Python Alomost a Circle Proyect """
import json
from json import encoder


class Base:
    """ Creat Class Base """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Comments test or checkcer """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    def integer_validator(self, name, value):
        """ Comments test or checkcer """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be > 0".format(name))

    def coordinate_validator(self, name, value):
        """ Comments test or checkcer """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value < 0:
            raise ValueError("{} must be >= 0".format(name))

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Comments test or checkcer """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return ("[]")
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Comments test or checkcer """
        filename = "{}.json".format(cls.__name__)
        with open(filename, 'w', encoding='utf-8') as f:
            listjson = []
            if list_objs is not None:
                for i in list_objs:
                    listjson.append(cls.to_dictionary(i))
                f.write(cls.to_json_string(listjson))
            else:
                f.write(cls.to_json_string(listjson))

    @staticmethod
    def from_json_string(json_string):
        """ Comments test or checker """
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)
