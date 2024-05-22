#!/usr/bin/python3
"""Function that add integer"""


def add_integer(a, b=98):
    """
    Args:
        a: an integer or a float.
        b: an integer or a float. Default to 98

    Returns:
        the addition of a and b

    Raises:
        TypeError: If a or b is not an iteger or a float
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
