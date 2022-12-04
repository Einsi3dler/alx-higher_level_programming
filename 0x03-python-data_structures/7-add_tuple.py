#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) < 2 or len(tuple_b) < 2:
        pass
    else:
        final_res = []
        tuple_a = list(tuple_a)
        tuple_b = list(tuple_b)
        final_res.append(tuple_a[0] + tuple_b[0])
        final_res.append(tuple_a[1] + tuple_b[1])
        return (tuple(final_res))
