#!/usr/bin/env python3
"""
Annotate the below function’s parameters and return
values with the appropriate types
"""
from typing import Sequence
def element_length(lst: list[Sequence]) -> list[tuple[Sequence, int]]:
    return [(i, len(i)) for i in lst]
