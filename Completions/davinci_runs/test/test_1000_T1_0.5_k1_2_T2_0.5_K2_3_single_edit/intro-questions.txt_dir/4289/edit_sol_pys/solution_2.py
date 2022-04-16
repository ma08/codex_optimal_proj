

import sys

n = int(sys.stdin.readline())
t, a = map(int, sys.stdin.readline().split())
h = [int(sys.stdin.readline()) for i in range(n)]


diff = []
for i in range(n):
    diff.append(abs(t - h[i] * 0.006 - a))

print(diff.index(min(diff)) + 1)
