#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    if idx < 0:
        return (None)
    a = len(my_list) - 1
    if idx > a:
        return my_list

    new_list = []

    for x in range(0,(a+1)):
        new_list.append(my_list[x])

    new_list[idx] = element

    return new_list
