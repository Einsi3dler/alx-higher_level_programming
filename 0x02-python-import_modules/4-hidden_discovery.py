#!/usr/bin/python3
import hidden_4


def module_reader():
    for i in dir(hidden_4):
        if not (i[0] == '_' and i[1] == '_'):
            print(i)


if __name__ == "__main__":
    module_reader()
