import sys


sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))[:n]

ans = [0] * n
for i in range(n):
    ans[a[i] - 1] = str(i + 1)

print(' '.join(ans))
