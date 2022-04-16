#!/usr/bin/env python3

import os
import sys

def main(args):
    b, k, g = [int(x) for x in args[1].split()][:3]
    days = 0
    while b > 0:
        days += 1
        b -= g
        if b < 0:
            break
        b -= k-g
    print(days)

if __name__ == '__main__':
    main(sys.argv)
