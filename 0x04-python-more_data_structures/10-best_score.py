#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    val = 0
    val_key = 'std'

    for key in a_dictionary:
        a = int (a_dictionary[key])
        if val > a :
            continue
        else:
            val = a_dictionary[key]
            val_key = key

    return val_key
