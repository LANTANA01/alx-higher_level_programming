#!/usr/bin/python3
"""Defines a Locked class."""


class LockedClass:
    """
    Prevent the user from instantiating new LockedClass attributes
    except 'first_name'.
    """

    __slots__ = ["first_name"]
