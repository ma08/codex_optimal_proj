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

    edges = [0] * (n - 1) # TODO: This is not a good way to do it.
    for i in range(n - 1): # TODO: This is not a good way to do it.
        edges[i] = list(map(int, sys.stdin.readline().split()))

    print(solve(n, k, edges))

def solve(n, k, edges):
    # TODO: Implement solution.
    pass

#------------------------------------------------------------------------------#

if __name__ == "__main__":
    main()
