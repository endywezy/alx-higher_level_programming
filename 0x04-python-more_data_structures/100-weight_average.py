#!/usr/bin/python3
# 100-weight_average.py

def weight_average(my_list=[]):
    """Return the weighted average of all integers in a list of tuples."""
    if not my_list or any(
        not isinstance(tup, tuple) or len(tup) != 2
        for tup in my_list
    ):
        return 0

    avg = sum(tup[0] * tup[1] for tup in my_list)
    size = sum(tup[1] for tup in my_list)

    return avg / size
