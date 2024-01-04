#!/usr/bin/python3

def uppercase(input_str):
    """Print a string in uppercase."""
    for c in input_str:
        print("{}".format(chr(ord(c) - 32) if 97 <= ord(c) <= 122 else c), end="")
    print("")
