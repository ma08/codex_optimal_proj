#!/usr/bin/env python3


def solve(n, k):
    return n, k


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        print(solve(n, k))
