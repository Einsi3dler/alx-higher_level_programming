#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        last_d = number % -10
        last_d = abs(last_d)
    elif number > 0:
        last_d = number % 10
    elif number < 10 and number >= 0:
        last_d = number
    print(f"{last_d}", end="")
    return last_d

