#!/usr/bin/python3
"""Define an inherited list class mylist"""


class MyList(list):
"""Implements sorted printing for the built-in list class"""

    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list)
