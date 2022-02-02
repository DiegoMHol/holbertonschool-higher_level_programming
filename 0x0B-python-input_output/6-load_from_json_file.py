#!/usr/bin/python3
""" Python Proyect """
import json


def load_from_json_file(filename):
    """ create an object from json file """
    with open(filename) as f:
        new_obj = json.load(f)
        return new_obj
