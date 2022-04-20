import sys
input = sys.stdin.readline


n, m = map(int, input().split())
a = list(map(int, input().split()))[:n]
b = list(map(int, input().split()))[:m]
c = []

ans = [0] * n
for i in range(n):
    ans[a[i] - 1] = i + 1
print(*ans)
