import sys
input = sys.stdin.readline().strip

n = int(input())
t, a = map(int, input().split())
h = [int(input()) for i in range(n)]

ans = 0
min_diff = 100000000
for i in range(n):
    diff = abs(t - h[i] * 0.006 - a)
    if diff < min_diff:
        min_diff = diff
        ans = i + 1

print(diff.index(min(diff)) + 1)
