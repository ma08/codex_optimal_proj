#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by techno at 3/05/19

#Feature:  #Enter feature name here
# Enter feature description here

#Scenario:  # Enter scenario name here
# Enter steps here

import sys

def main():
    n = int(input())
    x = list(map(int, input().split()))
    x.sort()
    if n % 2 == 0:
        print(x[n//2] - x[n//2 - 1])
    else:
        print(0)

if __name__ == "__main__":
    main()
