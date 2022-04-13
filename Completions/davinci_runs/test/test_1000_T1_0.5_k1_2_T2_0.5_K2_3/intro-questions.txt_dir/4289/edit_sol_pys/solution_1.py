
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = [int(input()) for i in range(n)]

dp = [[0 for i in range(m + 1)] for j in range(n + 1)]

print(diff.index(min(diff)) + 1)
