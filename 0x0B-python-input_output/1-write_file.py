#!/usr/bin/python3
""" Python Proyrect """


def write_file(filename="", text=""):
    """ Wrtie and return num of words """
    with open(filename, mode='w', encoding='utf-8') as f:
        return f.write(text)
