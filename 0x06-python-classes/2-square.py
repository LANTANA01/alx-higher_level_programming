#!/usr/bin/python3
"""Defines a class Square."""

class Square:
    """Represents a class Square."""
    def __init__(self, size=0):

        """Initializes a new Square.

        Args:
            size (int): The size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
