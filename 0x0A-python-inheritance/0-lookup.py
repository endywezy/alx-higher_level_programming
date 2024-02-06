#!/usr/bin/python3
"""define an object attribute"""

def lookup(obj):
    """Returns a list of available"""
    return [attr for attr in dir(obj) if not callable(getattr(obj, attr)) or not attr.startswith("__")]
