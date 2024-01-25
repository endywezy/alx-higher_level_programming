#!/usr/bin/python3
# 3-safe_print_division.py

def safe_print_division(a, b):
    """Returns the division of a by b and prints the result."""
    try:
        div = a / b
    except (TypeError, ZeroDivisionError):
        div = None
    finally:
        print("Inside result: {}".format(div))
    return div
