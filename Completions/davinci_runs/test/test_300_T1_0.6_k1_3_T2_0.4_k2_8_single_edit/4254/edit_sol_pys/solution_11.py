import sys

a, b = map(int, sys.stdin.readline().split())

if a <= b:
    print("unsafe")
else:
    print("safe")
