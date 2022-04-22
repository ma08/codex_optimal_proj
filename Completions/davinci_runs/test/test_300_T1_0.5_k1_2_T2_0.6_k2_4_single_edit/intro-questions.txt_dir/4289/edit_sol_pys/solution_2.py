import sys


input = sys.stdin.readline

n = int(input())
t, a = map(int, input().split())
h = [int(input()) for i in range(n)]

diff = [abs(t - h[i] * 0.006 - a) for i in range(n)]

print(diff.index(min(diff)) + 1)
