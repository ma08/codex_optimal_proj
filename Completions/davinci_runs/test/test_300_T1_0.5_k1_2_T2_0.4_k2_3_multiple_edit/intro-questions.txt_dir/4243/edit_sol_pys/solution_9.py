#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def max_happiness(x):
    """
    Args:
        x (int): the amount of yen that Takahashi has
    Returns:
        int: the maximum number of happiness points that can be earned
    """
    return x // 500 * 1000 + x % 500 // 5 * 5 # 500円玉で1000点、5円玉で5点

def main():
    x = int(sys.stdin.readline().rstrip())
    print(max_happiness(x))

if __name__ == '__main__':
    main()
