#!/usr/bin/env python3

import math

def euler(n):
    return sum(1/math.factorial(i) for i in range(n+1)) # n+1 because range is exclusive

if __name__ == '__main__':
    print(euler(int(input())))
