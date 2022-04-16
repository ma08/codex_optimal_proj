#!/usr/bin/env python3

import math

import sys

if __name__ == '__main__':
    x = int(sys.stdin.readline().strip())
    print(math.ceil(math.log(x, 2)))
