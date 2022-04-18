
import sys

input()

n, t, a = map(int, input().split())
h = list(map(int, input().split()))

diff = []
for i in range(n):
    diff.append(abs(t - h[i] * 0.006 - a))

print(diff.index(min(diff)) + 1)
