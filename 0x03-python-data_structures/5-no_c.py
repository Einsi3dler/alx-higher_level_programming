#!/usr/bin/python3
def no_c(my_string):
    my_string = list(my_string)
    for val in my_string:
        if val == 'c' or val == 'C':
            my_string.remove(val)
    return ''.join(my_string)
