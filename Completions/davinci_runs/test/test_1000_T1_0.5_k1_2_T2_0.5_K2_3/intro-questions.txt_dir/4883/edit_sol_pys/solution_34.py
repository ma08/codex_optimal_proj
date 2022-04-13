#!/usr/bin/env python3

import sys

def main():
    n = int(sys.stdin.readline())
    a = []
    for i in range(n):
        a.append(int(sys.stdin.readline()))
    a.sort()
    print(a[-1])

main()
