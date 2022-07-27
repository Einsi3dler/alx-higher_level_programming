#!/usr/bin/python3
def element_at(my_list, idx):

    a = len(my_list) - 1
    a = int(a)
    if (idx < 0) or (idx > a):
        return None
    else:
        return my_list[idx]
