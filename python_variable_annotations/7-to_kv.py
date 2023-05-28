#!/usr/bin/env python3
"""
sum_mixed_list which takes a list
mxd_lst of integers and floats and returns their sum as a float.
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    sum_mixed_list which takes a list
    mxd_lst of integers and floats and returns their sum as a float.
    """
    return k, float(v ** 2)
