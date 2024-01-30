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
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/set the width of the Rectangle."""
        return self._width

    @width.setter
    def width(self, value):
        self._validate_and_set_dimension('_width', value)

    @property
    def height(self):
        """Get/set the height of the Rectangle."""
        return self._height

    @height.setter
    def height(self, value):
        self._validate_and_set_dimension('_height', value)

    def area(self):
        """Return the area of the Rectangle."""
        return self._width * self._height

    def perimeter(self):
        """Return the perimeter of the Rectangle."""
        if self._width == 0 or self._height == 0:
            return 0
        return 2 * (self._width + self._height)

    def _validate_and_set_dimension(self, attribute, value):
        """Validate and set the width or height attribute."""
        if not isinstance(value, int):
            raise TypeError(f"{attribute[1:]} must be an integer")
        if value < 0:
            raise ValueError(f"{attribute[1:]} must be >= 0")
        setattr(self, attribute, value)
