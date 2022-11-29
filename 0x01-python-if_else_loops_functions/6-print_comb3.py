#!/usr/bin/python3
for num in range(0,9):
    if num == 8:
        print("89")
    else:
        for sub_num in range(num+1,10):
            print(f"{num}{sub_num}, ",end="")
