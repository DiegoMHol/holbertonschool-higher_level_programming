#!/usr/bin/python3
""" FIND PEAK """


def find_peak(list_of_integers):
    """ FIND PEAK """

    sort_list = []
    if len(list_of_integers) == 0:
        return None
    else:
        sort_list = sorted(list_of_integers)

        return (sort_list[len(sort_list) - 1])
