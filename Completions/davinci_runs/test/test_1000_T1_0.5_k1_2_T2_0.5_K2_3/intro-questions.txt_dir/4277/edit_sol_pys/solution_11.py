
import sys

n, a, b = list(map(int, sys.stdin.readline().split()))

print(min(n*a, b))
