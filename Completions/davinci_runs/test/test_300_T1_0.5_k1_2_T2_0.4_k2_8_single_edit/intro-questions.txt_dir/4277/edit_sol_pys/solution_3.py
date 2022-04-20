
import sys

n, a, b = map(int, sys.stdin.readline().split())  # n, a, b = input().split()

print(min(n * a, b))
