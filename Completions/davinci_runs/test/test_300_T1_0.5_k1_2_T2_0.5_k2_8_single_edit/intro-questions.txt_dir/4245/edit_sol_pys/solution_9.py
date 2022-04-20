

import sys

A, B = map(int, sys.stdin.readline().rstrip().split())
print(int((B // A) + (B % A != 0)))
