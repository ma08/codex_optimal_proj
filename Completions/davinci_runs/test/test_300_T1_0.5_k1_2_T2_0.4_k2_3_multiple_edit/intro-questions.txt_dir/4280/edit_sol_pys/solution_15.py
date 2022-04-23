#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------#
#  file: file.py                                                               #
#  brief:                                                                      #
#                                                                              #
#  author: Oleg Burdaev                                                        #
#  date:   26 Mar 2020                                                         #
#------------------------------------------------------------------------------#

#------------------------------------------------------------------------------#

import sys

def main():
    n, k = map(int, sys.stdin.readline().split())

    edges = []
    for _ in range(n - 1):
        edges.append(list(map(int, sys.stdin.readline().split())))

    print(solve(n, k, edges))

def solve(n, k, edges):
    # TODO: Implement solution.
    pass

#------------------------------------------------------------------------------#

if __name__ == "__main__":
    main()
