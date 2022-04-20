import sys
import math

a, b, c = map(int, sys.stdin.readline().split())

print(a + b + c - max(a, b, c) - min(a, b, c))
