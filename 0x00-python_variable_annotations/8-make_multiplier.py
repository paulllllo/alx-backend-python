#!/usr/bin/env python3
""" A module that defines complex type annotations- callable """

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    def func(x: float, y: float = multiplier) -> float:
        return x * y
    return func
