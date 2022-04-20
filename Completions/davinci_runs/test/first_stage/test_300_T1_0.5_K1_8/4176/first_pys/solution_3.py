

import sys

a, b = map(int, sys.stdin.readline().rstrip().split())

if a > b:
    a, b = b, a

for i in range(1, b+1):
    if a * i % b == 0:
        print(a * i)
        exit(0)