

# SOLUTION

import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    if n == 1:
        print(0)
    else:
        print((n-1)//2)