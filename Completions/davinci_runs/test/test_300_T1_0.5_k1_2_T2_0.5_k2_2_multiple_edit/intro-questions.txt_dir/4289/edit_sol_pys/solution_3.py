
import sys

input = sys.stdin.readline

n = int(input())
T, A = map(int, input().split())
h = [int(input()) for i in range(n)]

diff = []
for i in range(n):
    diff.append(abs(T - h[i] * 0.006 - A))

print(diff.index(min(diff)) + 1)
