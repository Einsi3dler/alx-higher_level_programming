#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list == None:
        return
    else:
        listLen = len(my_list) - 1
        for num in range(listLen, -1, -1):
            print("{:d}".format(my_list[num]))
