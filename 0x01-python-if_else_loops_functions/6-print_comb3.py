#!/usr/bin/python3
for num in range(0, 9):
    if num == 8:
        print("{}".format(89))
    else:
        for sub_num in range(num+1, 10):
            print("{}{}, ".format(num, sub_num), end="")
