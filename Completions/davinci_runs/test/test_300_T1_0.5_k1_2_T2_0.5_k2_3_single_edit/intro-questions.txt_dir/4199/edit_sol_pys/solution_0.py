#!/usr/bin/env python3
# -*- coding: utf-8 -*-



def resolve():
    n, k = map(int, input().split())
    h = [int(input()) for _ in range(n)]
    print(sum(1 if i >= k else 0 for i in h))


if __name__ == "__main__":
    resolve()
