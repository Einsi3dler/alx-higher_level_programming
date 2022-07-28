#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    val_store = []
    for key in a_dictionary:
        val_store.append(key)
    val_store.sort()

    for key in val_store:
        print("{}: {}".format(key,a_dictionary[key]))
