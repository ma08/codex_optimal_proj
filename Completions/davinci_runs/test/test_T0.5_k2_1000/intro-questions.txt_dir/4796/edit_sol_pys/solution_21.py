
import sys
import math

a, b, c = map(float, sys.stdin.readline().split())
i, j, k = map(float, sys.stdin.readline().split())
x = min(a/i, b/j, c/k)

print(str(int(a - x * i)) + " " + str(int(b - x * j)) + " " + str(int(c - x * k)))
