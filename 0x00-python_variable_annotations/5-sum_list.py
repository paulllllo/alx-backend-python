#!/usr/bin/env python3
""" A module that defines basic type annotations """

from typing import List


def sum_list(input_list: List[float]) -> float:
    """A function that returns the sum of floats in a list"""
    return sum(input_list)
