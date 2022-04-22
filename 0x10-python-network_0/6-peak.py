#!/usr/bin/python3
""" FIND PEAK OF LIST OF INT """

def find_peak(list_of_integers):
    """ FIND PEAK """
    lenList = len(list_of_integers)
    if lenList < 3:
        return None
    peak = list_of_integers[1]
    for i in range(1, lenList):
        if list_of_integers[i] >= peak:
            peak = list_of_integers[i]
    return peak
