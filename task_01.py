#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A new Fibonacci sequence generator"""


def xfibo(count):
    """Fibo seq. gen.

    Args:
        count (int): integers

    Returns:
        list: fibo sequence

    Examples:
        >>> for x in xfibo(5):
                print x

        0
        1
        1
        2
        3
    """
    start = 0
    last_num, cur_num = 0, 1
    yield last_num
    while start < count - 1:
        yield cur_num
        last_num, cur_num = cur_num, last_num + cur_num
        start += 1
