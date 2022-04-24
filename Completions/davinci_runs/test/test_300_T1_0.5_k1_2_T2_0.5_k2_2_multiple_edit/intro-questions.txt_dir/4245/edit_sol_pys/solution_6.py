# coding=utf-8

import sys

A, B, C = map(int, sys.stdin.readline().rstrip().split())
print(C // A + (C % A != 0))
