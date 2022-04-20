# -*- coding: utf-8 -*-

import sys

n = int(sys.stdin.readline())
line = [int(i) for i in sys.stdin.readline().split()]

print(n, line)

if max(line) < sum(line) - max(line):
    print("Yes")
else:
    print("No")
