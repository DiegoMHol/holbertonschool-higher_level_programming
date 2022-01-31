#!/usr/bin/python3
""" Python proyect """


def inherits_from(obj, a_class):
    """ Is a calss inheritnanhe """
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    else:
        return False
