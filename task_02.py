#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""a list comprehension"""

import task_01


def fibo(count):
    """
    Uses task_01.xfibo() to generate count Fibonacci numbers
    and return them all in a list.

    Args:
        count (int): amount of nums in the seq.

    Returns:
        list: of the fib seq.

    Examples:
        >>> fibo(5)
        [0, 1, 1, 2, 3]
    """
    return [x for x in task_01.xfibo(count)]
