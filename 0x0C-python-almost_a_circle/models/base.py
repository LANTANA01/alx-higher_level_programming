#!/usr/bin/python3

"""Defines a base model module."""

class Base:
    """Represent a base model class.

    This is the "base" for all other classes in project 0x0C*.

    Private Class Attributes:
        __nb_object (int): Number of instantiated Bases or Objects.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base obj.

        Args:
            id (int): The key identifier of the new Base obj created.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
