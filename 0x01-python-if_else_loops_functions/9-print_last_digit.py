#!/usr/bin/python3
def print_last_digit(number):
    if (number < 0):
        i = number % -10 * -1
    else:
        i = number % 10
    print("{:d}".format(i), end="")
    return (i)
