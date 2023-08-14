#!/usr/bin/env python3
"""
Checks if the given object is an instance of, or an instance of a class inherited from, the specified class.
"""
def is_kind_of_class(obj, a_class):
    """
    Checks if the given object is an instance of, or an instance of a class inherited from, the specified class.

    Args:
        obj: The object to be checked.
        a_class: The class to compare against.

    Returns:
        bool: True if the object is an instance of the specified class or its subclasses, otherwise False.
    """
    return isinstance(obj, a_class)
