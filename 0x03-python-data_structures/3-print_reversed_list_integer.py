#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    a = len(my_list) - 1

    while (a != -1):
        print("{}".format(my_list[a]))
        a = a-1


