#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    cl_int_leng = len(sys.argv)
    if cl_int_leng-1 == 0:
        print("{} arguments.".format(cl_int_leng-1))
    else:
        print("{} arguments:".format(cl_int_leng-1))
        num = 0
        for val in sys.argv:
            if num == 0:
                pass
            else:
                print("{}: {}".format(num, val))
            num = num + 1
