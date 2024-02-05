#!/usr/bin/python3
"""Defines a function that checks for a class."""


def is_same_class(obj, a_class):
    """This checks if an object is exactly an instance of a given class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        If obj is exactly an instance of a_class - Returns true.
        Otherwise - False.
    """
    if type(obj) == a_class:
        return True
