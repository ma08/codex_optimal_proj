#!/usr/bin/env python3

import sys

def main(k):
    a, b = 0, 1
    for _ in range(k):
        a, b = b, a + b
    return a, b

if __name__ == "__main__":
    k = int(sys.stdin.readline())
    a, b = main(k)
    print(a, b)
