#!/usr/bin/python3
def uppercase(str):
    final = ""
    for c in str:
        alpha_var = ord(c)
        if alpha_var >= 97 and alpha_var <= 122:
            alpha_var = alpha_var - 32
            alpha_var = chr(alpha_var)
            final = final + alpha_var
        else:
            final = final + c
    print("{}".format(final))
