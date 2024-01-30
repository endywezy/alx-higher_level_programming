#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Represent a rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        self._width = 0
        self._height = 0
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self._width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle."""
        self._validate_and_set_dimension("_width", value)

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self._height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle."""
        self._validate_and_set_dimension("_height", value)

    def _validate_and_set_dimension(self, attr_name, value):
        """Validate and set the width or height."""
        if not isinstance(value, int):
            raise TypeError(f"{attr_name[1:]} must be an integer")
        if value < 0:
            raise ValueError(f"{attr_name[1:]} must be >= 0")
        setattr(self, attr_name, value)

