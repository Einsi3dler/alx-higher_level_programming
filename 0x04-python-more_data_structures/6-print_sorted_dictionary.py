#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    keys = []
    for k, v in a_dictionary.items():
        keys.append(k)
    keys.sort()
    for val in keys:
        print(f"{val}: {a_dictionary[val]}")
