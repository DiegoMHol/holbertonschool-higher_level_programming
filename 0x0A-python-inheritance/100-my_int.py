#!/usr/bin/python3
""" Python advanced proy """


class MyInt(int):
    """ Inverted == and != """
    def __eq__(inv, des):
        return inv is des

    def __ne__(inv, des):
        return inv is not des
