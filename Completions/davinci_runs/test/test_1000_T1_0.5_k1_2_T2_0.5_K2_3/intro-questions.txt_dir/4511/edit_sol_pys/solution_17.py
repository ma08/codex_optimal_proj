# coding: utf-8

import sys
import math

def main():
    a, b, c = [int(x) for x in input().split()]
    p = (a + b + c) / 2
    print(math.sqrt(p * (p - a) * (p - b) * (p - c)))

if __name__ == "__main__":
    main()
