#!/usr/bin/env python3
""" A module that shows definition of a typevar """

from typing import TypeVar, Mapping, Any, Union, Any

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """A function that safely gets a value"""
    if key in dct:
        return dct[key]
    else:
        return default
