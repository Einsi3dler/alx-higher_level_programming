#!/usr/bin/python3
def uniq_add(my_list=[]):
    num_sum = 0
    no_dup = set(my_list)
    no_dup = list(no_dup)
    for num in no_dup:
        num_sum += num
    return num_sum
