#!/usr/bin/python3
# 1-safe_print_integer.py

def safe_print_integer(value):
    """Print an integer with "{:d}".format().

    Args:
        value (int): The integer to print.

    Returns:
        True if successful, False if a TypeError or ValueError occurs.
    """
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError):
        return False
