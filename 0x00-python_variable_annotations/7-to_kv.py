#!/usr/bin/env python3
""" A module that defines complex annotation types """

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """A function that returns a tuple of different typed args"""
    return (k, float(v ** 2))
