import sys
sys.setrecursionlimit(10 ** 7)

n = int(input())
h = list(map(int, input().split()))

def dfs(i):
    if i == n:
        return True
    if h[i] == 0:
        return dfs(i + 1)
    if i + 1 < n and h[i + 1] > 0:
        return False
    if i + 2 < n and h[i + 2] > 0:
        return False
    h[i] -= 1
    if not dfs(i):
        return False
    h[i] += 1

    if i + 1 < n and h[i + 1] > 0:
        h[i + 1] -= 1
        if not dfs(i + 1):
            return False
        h[i + 1] += 1

    if i + 2 < n and h[i + 2] > 0:
        h[i + 2] -= 1
        if not dfs(i + 2):
            return False
        h[i + 2] += 1

    return True


if dfs(0):
    print("Yes")
else:
    print("No")
