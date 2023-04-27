#!/usr/bin/env python3
"""
Use mypy to validate the following piece of code and
apply any necessary changes.
"""
from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    lst : Tuple
    """
    zoomed_in: list[int] = [
        item for item in lst
        for i in range(int(factor))
    ]
    return zoomed_in
