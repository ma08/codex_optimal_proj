#!/usr/bin/env python3


def solve(n):
    return n + 1


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(solve(n))
