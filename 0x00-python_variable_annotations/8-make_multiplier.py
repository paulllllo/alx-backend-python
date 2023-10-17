#!/usr/bin/env python3
""" A module that defines complex type annotations- callable """

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """A function that returns a multiplier callback"""
    def func(x: float, y: float = multiplier) -> float:
        """A function that multiplies a float arg with the multiplier"""
        return x * y
    return func
