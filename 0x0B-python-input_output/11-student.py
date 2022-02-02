#!/usr/bin/python3
""" Python Proyect """


class Student:
    """ Create a strudent class """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if not isinstance(attrs, list):
            return self.__dict__
        for i in attrs:
            if not isinstance(i, str):
                return self.__dict__
        dic = {}
        for j in attrs:
            if j in self.__dict__.keys():
                dic[j] = self.__dict__[j]
        return dic

    def reload_from_json(self, json):
        for i in json:
            self.__dict__[i] = json[i]
