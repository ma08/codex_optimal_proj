#!/usr/bin/python
# -*- coding: utf-8 -*-
import math

def f(x):
    """
    :param x:
    :return:
    """
    return math.exp(x * math.log(2)) - 2

def main():
    """
    :return:
    """
    n = float(input())
    l, r = 0.0, 2.0

    while r - l > 1e-9:
        m = (l + r) / 2
        if f(m) < 0:
            l = m
        else:
            r = m

    print(l)

if __name__ == "__main__":
    main()
