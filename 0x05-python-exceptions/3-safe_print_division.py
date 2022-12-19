#!/usr/bin/python3
def safe_print_division(a, b):
    div_ = None
    try:
        div_ = a / b
    except ZeroDivisionError:
        return None
    else:
        return div_
    finally:
        print("Inside result: {}".format(div_))
