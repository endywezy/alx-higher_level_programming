#!/usr/bin/python3
# 4-new_in_list.py

def new_in_list(my_list, idx, element):
    """Replace an element in a copied list at a specific position."""
    if 0 <= idx < len(my_list):
        copy = my_list[:]
        copy[idx] = element
        return copy

    return my_list
