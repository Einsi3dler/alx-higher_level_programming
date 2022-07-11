#!/usr/bin/python3
def uppercase(str):
    for x in str:
        a = ord(x)
        if a == 32 or (a >= 65 and a <= 90) or (a >= 33 and a <= 64):
            a = chr(a)
        else:
            a = a - 32
            a = chr(a)
        print("{}".format(a), end="")
    print("")
