#!/usr/bin/python3
# 1-search_replace.py

def search_replace(my_list, search, replace):
    """Replace all occurrences of an element by another in a new list."""
    return [replace if x == search else x for x in my_list]
