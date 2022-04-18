#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 20:37:00 2019
@author: alex
"""
import sys

def main():
    num_cases = int(sys.stdin.readline().strip())
    for i in range(num_cases):
        n = int(sys.stdin.readline().strip())
        shuffle = sys.stdin.readline().strip()
        if shuffle == 'out':
            print(n//2)
        else:
            print(n-1)


if __name__ == '__main__':
    main()
