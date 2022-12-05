#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    final_res = []
    tuple_a, tuple_b = list(tuple_a), list(tuple_b)
    tuple_a.extend([0, 0])
    tuple_b.extend([0, 0])
    final_res.extend([(tuple_a[0] + tuple_b[0]), (tuple_a[1] + tuple_b[1])])
    return (tuple(final_res))
