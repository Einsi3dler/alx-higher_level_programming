#!/bin/python3
import hidden_4
my_list = dir(hidden_4)
my_list.sort()
for x in my_list:
    if x[0] == '_':
        continue
    else:
        print("{}".format(x))

