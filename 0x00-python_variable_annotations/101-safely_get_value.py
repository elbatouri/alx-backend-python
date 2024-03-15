#!/usr/bin/env python3
"""Contains method that safely gets value from dictionary."""
from typing import Mapping, Any, Union, TypeVar, Optional

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Optional[T] = None) -> Union[Any, T]:
    """Safely gets value from dictionary.
    Args:
        dct (dict): Dictionry from where to get value.
        key (str): Key to get value.
        default (any): Default value if key not found.
    Returns:
        Value from dictionary.
    """
    if key in dct:
        return dct[key]
    else:
        return default
