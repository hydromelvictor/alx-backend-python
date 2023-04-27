#!/usr/bin/env python3
"""
Use mypy to validate the following piece of code and
apply any necessary changes.
"""

def zoom_array(lst: list[int], factor: float = 2) -> list[int]:
    zoomed_in: list[int] = [
        item for item in lst
        for i in range(int(factor))
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3.0)
