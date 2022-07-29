#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    a = len((sys.argv))
    val = 1
    my_list =  (sys.argv)
    if a == 1:
        print("{} arguments.".format(a-1))
    else:
        print("{} arguments:".format(a-1))
        while val < a:
            print("{}: {}".format(val, my_list[val]))
            val = val + 1
