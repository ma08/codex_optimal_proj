# coding: utf-8

import sys
import io

def resolve():
    n = int(input())
    names = []
    for _ in range(n):
        names.append(input())

    if names == sorted(names):
        print("INCREASING")
    elif names == sorted(names, reverse=True):
        print("DECREASING")
    else:
        print("NEITHER")

if __name__ == "__main__":
    sys.stdin = io.StringIO(sys.stdin.read())
    resolve()
