#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
a1 = 10
a2 = -10
a_str = "Last digit of"
b_str = "less than 6 and not 0"
if number >= 0:
    last_num = number % a1
else:
    last_num = number % a2

if last_num > 5:
    print("{} {} is {} and is greater than 5".format(a_str, number, last_num))
elif last_num < 6 and last_num != 0:
    print("{} {} is {} and is {}".format(a_str, number, last_num, b_str))
else:
    print("{} {} is {} and is 0".format(a_str, number, last_num))
