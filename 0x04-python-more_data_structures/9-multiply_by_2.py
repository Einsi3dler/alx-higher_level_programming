#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    tmpval = []
    key = []

    for a in a_dictionary:
        key.append(a)
        tmpval.append(a_dictionary[a])

    val = list(map(lambda x:x*2,tmpval))

    new_dict = dict(zip(key,val))
    return new_dict

