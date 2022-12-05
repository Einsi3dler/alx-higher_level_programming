#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    final_lis = []
    for num in my_list:
        if num % 2 == 0:
            final_lis.append(True)
        else:
            final_lis.append(False)
    return final_lis
