import sys
from math import fabs
input = sys.stdin.readline

n = int(input())
t, a = map(int, input().split())
h = [int(input()) for i in range(n)]

diff = []
for i in range(n):
    diff.append(fabs(t - h[i] * 0.006 - a))

print(diff.index(min(diff)) + 1)
