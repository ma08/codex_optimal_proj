# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 19:03:17 2020

@author: LENOVO
"""


def solve(n, s):
    counter = 0
    for i in s:
        counter += i - 1
    return counter


if __name__ == '__main__':
    n = int(input())
    s = input()
    print(solve(n, s))
