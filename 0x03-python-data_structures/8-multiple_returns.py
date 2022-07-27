#!/usr/bin/python3

def multiple_returns(sentence):
    a = list(sentence)
    b = [ ]

    if len(a) < 1:
        return None

    b.append(len(a))
    b.append(a[0])

    b = tuple(b)

    return b
