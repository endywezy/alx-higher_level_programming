#!/usr/bin/python3

"""defines blocked class."""
class LockedClass:
    """
    Prevent the user from instantiating new LockedClass attributes
    for anything but attributes called 'first_name'.
    """

    __slots__ = ['first_name']
    def __init__(self):
        pass
