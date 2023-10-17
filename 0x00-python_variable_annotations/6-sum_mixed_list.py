#!/usr/bin/env python3
""" A module that defines complex annotation types- mixed list """

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """A function that sums a list of mixed int and float types"""
    return float(sum(mxd_lst))
