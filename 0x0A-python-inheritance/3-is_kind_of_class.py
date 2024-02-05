#!/usr/bin/python3
"""Defines a functionthat checks fo an inherited class."""


def is_kind_of_class(obj, a_class):
    """This checks if an object is an instance or inherited instance of a class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        If obj is an instance or inherited instance of a_class - Returns true.
        Otherwise - False.
    """
    if isinstance(obj, a_class):
        return True
