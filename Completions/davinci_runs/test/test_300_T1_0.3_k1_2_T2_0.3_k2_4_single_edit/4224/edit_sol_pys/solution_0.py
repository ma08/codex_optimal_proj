

import sys
sys.setrecursionlimit(10**7)

def dfs(i, n, a, count):
    if i == n:
        return count

    if a[i] % 2 == 0:
        a[i] /= 2
        return dfs(i+1, n, a, count+1)
    else:
        return count

n = int(input())
a = list(map(int, input().split()))

print(dfs(0, n, a, 0))
