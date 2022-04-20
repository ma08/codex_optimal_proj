

import sys

a, b, k = map(int, sys.stdin.readline().split())

if a > b:
    a, b = b, a

for i in range(a, 0, -1):
    if a % i == 0 and b % i == 0:
        k -= 1
        if k == 0:
            print(i)
            break