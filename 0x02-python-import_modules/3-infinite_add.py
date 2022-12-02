#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    num = 0
    final_val = 0
    for val in sys.argv:
        if num == 0:
            pass
        else:
            final_val = final_val + int(val)
        num = num + 1
    print(final_val)
