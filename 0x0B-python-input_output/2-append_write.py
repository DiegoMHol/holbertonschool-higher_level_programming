#!/usr/bin/python3
""" Python Proyect """


def append_write(filename="", text=""):
    """ Append text to file """
    with open(filename, mode='a', encoding='utf-8') as f:
        return f.write(text)
