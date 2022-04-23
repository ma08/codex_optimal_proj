import sys

input = sys.stdin.readline()

n = int(input())
t, a = map(int, input().strip().split())
h = [int(input()) for _ in range(n)]

diff = []
for i in range(n):
    diff.append(abs(t - h[i] * 0.006 - a))

print(diff.index(min(diff)) + 1)
