#!/usr/bin/python3
def search_replace(my_list, search, replace):
    res_arr = []
    for val in my_list:
        if val == search:
            res_arr.append(replace)
        else:
            res_arr.append(val)
    return res_arr
