#!/usr/bin/python3
"""Define an inherited list class mylist"""


class MyList(list):

    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list)
