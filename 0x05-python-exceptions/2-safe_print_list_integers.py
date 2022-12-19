#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    ind = x
    val_t = 0
    for num in range(ind):
        try:
            if (type(my_list[num]) is int):
                print("{:d}".format(my_list[num]), end="")
                val_t = val_t + 1
            else:
                continue
        except (IndexError, TypeError, NameError):
            break
    print()
    return val_t
