import sys

A, B = map(int, sys.stdin.readline().rstrip().split())
print((B - 1) // A + 1)
