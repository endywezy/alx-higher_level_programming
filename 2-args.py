#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    length = len(argv) - 1

    if length == 0:
        print("0 arguments.")
    elif length == 1:
        print("1 argument:")
        print("1: {}".format(argv[1]))
    else:
        print("{:d} arguments:".format(length))
        for i in range(1, length + 1):
            print("{:d}: {}".format(i, argv[i]))
