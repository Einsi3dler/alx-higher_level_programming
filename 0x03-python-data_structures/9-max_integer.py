#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) < 1:
        return None
    else:
        my_list.sort()
        final_val = my_list[-1]
        return final_val
