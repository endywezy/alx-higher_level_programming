#!/usr/bin/python3
# 10-divisible_by_2.py
# Brennan D Baraban <375@holbertonschool.com>

def divisible_by_2(my_list=[]):
    """Find all multiples of 2 in a list."""
    return [num % 2 == 0 for num in my_list]
