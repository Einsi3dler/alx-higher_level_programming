#!/usr/bin/python3
def uniq_add(my_list=[]):
    a = set(my_list)
    a = list(a)
    sum_ = 0

    for x in a:
        sum_ = x + sum_

    return sum_
