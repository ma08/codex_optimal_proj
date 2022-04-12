#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 13:25:01 2020
@author: krishna
"""

import sys

def main():
    start = [int(i) for i in sys.stdin.readline().split()] #list comprehension
    end = [int(i) for i in sys.stdin.readline().split()] #list comprehension
    charge = int(sys.stdin.readline())
    if (charge - abs(end[0] - start[0]) - abs(end[1] - start[1])) % 2 == 0: #abs() returns absolute value of a number
        print("Y")
    else:
        print("N")

if __name__ == "__main__":
    main()
