#!/usr/bin/python3

def search_replace(my_list, search, replace):
    new_list = my_list.copy()

    i = 0

    for x in new_list:
        if x == search:
            new_list[i] = replace
        i = 1 + i

    return new_list 
