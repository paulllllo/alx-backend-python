#!/usr/bin/env python3
"""A module that defines complex type annotations - duck typing"""

from typing import Sequence, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Returns first item in a sequence"""
    if lst:
        return lst[0]
    else:
        return None
