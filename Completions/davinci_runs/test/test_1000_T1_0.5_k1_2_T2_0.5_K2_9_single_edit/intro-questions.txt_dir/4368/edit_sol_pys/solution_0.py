#!/usr/bin/env python3

from math import log

n, k = map(int, input().split())
print(int(log(n, k)) + 1)
