#!/usr/bin/python3
"""Defines the add Integer module."""


def add_integer(a, b=98):
    """
    This function adds two integer/float a and b.

    Args:
        a(integer/float): This is the first number.
        b(integer/float): This is the second number.

    Returns:
        int: the sum of a and b in int.

    Raises:
        TypeError: If either of a or b is a non-integer and non-float.
    """

    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
