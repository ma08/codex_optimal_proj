

import sys
import math
input = sys.stdin.readline

n = int(input())
t, a = map(int, input().split())
h = [int(input()) for i in range(n)]

diff = []
for i in range(n):
    diff.append(abs(t - h[i] * 0.006 - a))  # abs:absolute value

print(diff.index(min(diff)) + 1)
