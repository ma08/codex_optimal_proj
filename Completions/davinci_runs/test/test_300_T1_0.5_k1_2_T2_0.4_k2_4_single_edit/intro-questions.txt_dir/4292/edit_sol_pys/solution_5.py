#!/usr/bin/python3

import sys

n, k = map(int, sys.stdin.readline().split())
p = list(map(int, sys.stdin.readline().split()))

print(sum(sorted(p)[:k]))
