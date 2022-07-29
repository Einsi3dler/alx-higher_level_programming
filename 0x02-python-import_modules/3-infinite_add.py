#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    addition = 0
    ind = 1
    my_list = (sys.argv)
    list_len = len((sys.argv))
    
    while (ind < list_len):
        a = int(my_list[ind])
        addition = addition + a
        ind = ind + 1
    print("{}".format(addition))

