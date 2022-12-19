#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    def checker(y, z):
        if y > z:
            return y
        else:
            return z
    list_len = checker(len(my_list_1), len(my_list_2))
    res_lis = []

    for val in range(list_length):
        try:
            temp = my_list_1[val]/my_list_2[val]
            res_lis.append(temp)
        except IndexError:
            print("out of range")
            res_lis.append(0)
            continue
        except ZeroDivisionError:
            print("division by 0")
            res_lis.append(0)
            continue
        except TypeError:
            print("wrong type")
            res_lis.append(0)
            continue
        finally:
            continue
    return res_lis
