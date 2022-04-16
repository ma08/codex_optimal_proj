#!/usr/bin/env python3

import sys
import math

def main():
    h, v = map(float, sys.stdin.readline().split())
    print(math.ceil(h / math.sin(math.radians(v)))) 

if __name__ == '__main__':
    main()
