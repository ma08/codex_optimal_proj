#!/usr/bin/python

import sys
import os
import subprocess

def main():
    n = int(input())
    a = list(map(int, input().split()))

    # find indices of all elements with value of 2
    indices = [i for i, x in enumerate(a) if x == 2]

if __name__ == "__main__":
    main()
