#!/usr/bin/python3
"""Defines attributes present in lookup function."""


def lookup(obj):
    """Returns a list of available attributes in an object."""
    return (dir(obj))
