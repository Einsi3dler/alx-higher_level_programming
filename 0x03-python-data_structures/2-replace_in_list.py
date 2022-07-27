#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    a = len(my_list) - 1
    a = int(a)
    
    if (idx < 0):
        return (None)

    if(idx > a):
        return (my_list)

    my_list[idx] = element

    return (my_list)
