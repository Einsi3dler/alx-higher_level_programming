#!/usr/bin/
def no_c(my_string):
    p = list(my_string)
    for x in my_string:
        if x == "C":
            p.remove(x)
        elif x == "c":
            p.remove(x)
    p = ''.join(p)
    return(p)
