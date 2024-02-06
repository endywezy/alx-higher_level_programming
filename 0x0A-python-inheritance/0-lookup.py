#!/usr/bin/python3

def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    Args:
        obj (object): The input object.

    Returns:
        list: A list containing the names of attributes and methods.
    """
    return [attr for attr in dir(obj) if not callable(getattr(obj, attr)) or not attr.startswith("__")]
