#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or (len(my_list) - 1) < idx:
        return None
    else:
        new_list = []
        for val in my_list:
            new_list.append(val)
        new_list[idx] = element
        return new_list
