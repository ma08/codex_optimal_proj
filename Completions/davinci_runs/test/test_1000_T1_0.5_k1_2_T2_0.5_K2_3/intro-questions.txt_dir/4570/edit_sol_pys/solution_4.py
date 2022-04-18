
import sys

A, B = map(int, sys.stdin.readline().split())

if A < B:
    print("0")
else:
    print(A - B)
