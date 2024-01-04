#!/usr/bin/python3
# 102-magic_calculation.py
# Brennan D Baraban <375@holbertonschool.com>

def magic_calculation(a, b, c):
    """Match bytecode provided by Holberton School."""
    if a < b:
        return c
    elif c > b:
        return a + b
    else:
        return (a * b - c)
