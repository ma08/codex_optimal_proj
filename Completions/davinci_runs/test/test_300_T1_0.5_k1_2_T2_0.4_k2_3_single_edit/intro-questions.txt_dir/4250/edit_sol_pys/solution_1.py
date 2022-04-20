#!/usr/bin/env python3

import sys
n, k = map(int, input().split())
s = list(map(int, input().split()))
s = sorted(s)
print(s[-k])
