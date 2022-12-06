#!/usr/bin/python3
def no_c(my_string):
    my_string = list(my_string)
    ind = 0
    val_len = len(my_string)
    while val_len > ind:
        if my_string[ind] == 'c' or my_string[ind] == 'C':
            del my_string[ind]
            ind = ind - 1
            val_len = val_len - 1
        ind = ind + 1
    return ''.join(my_string)
