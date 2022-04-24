# coding=utf-8

import sys

a, b = map(int, sys.stdin.readline().rstrip().split())
print(b // a + (b % a != 0))
