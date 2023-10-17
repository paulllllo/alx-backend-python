#!/usr/bin/env python3
""" A module that defines type annotations - Iterable, Sequence """

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """A function that returns a list of tuples for items in an iterable"""
    return [(i, len(i)) for i in lst]
