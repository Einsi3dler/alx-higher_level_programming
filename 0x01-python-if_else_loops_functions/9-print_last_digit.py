#!/usr/bin/python3
def print_last_digit(number):
    a1 = 10
    a2 = -10
    if number >= 0:
        last_num = number % a1
        print(last_num)
        return last_num
    else:
        last_num = number % a2
        print(last_num)
        return last_num
