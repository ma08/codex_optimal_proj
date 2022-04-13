#!/usr/bin/env python3

import sys

def main():
    m, n = map(int, sys.stdin.readline().split())
    d = dict()
    for i in range(m):
        a, b = sys.stdin.readline().split()[0], sys.stdin.readline().split()[0]
        d[a] = b
    for i in range(n):
        a, b = sys.stdin.readline().split()[0], sys.stdin.readline().split()[0]
        if len(a) != len(b):
            print("no")
            continue
        a = list(a)
        b = list(b)
        for i in range(len(a)):
            if a[i] in d:
                if b[i] in d[a[i]]:
                    continue
                else:
                    print("no")
                    break
            else:
                print("no")
                break
        else:
            print("yes")

main()
