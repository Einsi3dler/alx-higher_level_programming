#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    a = list(tuple_a)
    b = list(tuple_b)
    
    d = [0,0]

    c = [0,0]

    c[0] = len(a)
    c[1] = len(b)

    if c[0] < 2:
        a.append(0)
    if c[1] < 2:
        b.append(0)

    if c[0] < 1:
        a.append(0)
        a.append(0)

    if c[1] < 1:
        b.append(0)
        b.append(0)

    for g in (a,b):
       d[0] = a[0] + b[0]
       d[1] = a[1] + b[1]

    d = tuple(d)

    return (d)
