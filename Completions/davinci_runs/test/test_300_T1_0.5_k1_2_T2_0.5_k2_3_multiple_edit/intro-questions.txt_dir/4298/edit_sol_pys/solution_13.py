#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

def main():
    N, D = map(int, input().split())
    if N <= D:
        print(1)
    else:
        print(math.ceil((N - D) / (2 * D + 1)) + 1)

if __name__ == "__main__":
    main()
