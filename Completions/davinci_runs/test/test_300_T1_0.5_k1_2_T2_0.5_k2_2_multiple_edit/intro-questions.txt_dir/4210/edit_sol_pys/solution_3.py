import sys
sys.setrecursionlimit(10**6)
n, k = map(int, input().split())
a = list(map(int, input().split()))
s = [0] * n
s[0] = a[0]
for i in range(1, n):
    s[i] = s[i-1] + a[i]

def check_sum(x, y, k):
    if x == 0:
        return s[y] % k == 0
    return (s[y] - s[x-1]) % k == 0

def dfs(x):
    if x == n:
        return 0
    for i in range(x, n):
        if check_sum(x, i, k):
            return dfs(i+1) + 1
    return 0
print(dfs(0))
