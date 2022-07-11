#!/usr/bin/python3
def pow(a, b):
    exp = 1
    if b == 0:
        return exp
    elif b==1:
        return a
    elif b < 0:
        b = abs(b)
        for x in range(0,b):
            exp = exp  * (1/a)
        return exp
    elif b > 0:
        for x in range(0,b):
            exp = exp * a
        return exp
