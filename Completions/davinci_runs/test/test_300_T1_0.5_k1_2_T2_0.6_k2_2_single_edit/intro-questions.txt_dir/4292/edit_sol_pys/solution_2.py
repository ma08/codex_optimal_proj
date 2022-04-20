
import sys
import math

n, a, b = map(int, sys.stdin.readline().split())

print(math.floor((n-1)*a+b))
