#!/usr/bin/env python

import sys
n, a, b = map(int, sys.stdin.readline().split())

print(min(n*a, b))
