N, A, B, C = map(int, input().split())
l = [int(input()) for _ in range(N)]
INF = float('inf')


def dfs(cur, a, b, c):
    if cur == N:
        if a > 0 and b > 0 and c > 0:
            return abs(A - a) + abs(B - b) + abs(C - c) - 30
        else:
            return INF

    res = INF
    res = min(res, dfs(cur + 1, a, b, c) + 7)
    res = min(res, dfs(cur + 1, a + l[cur], b, c) + 10)
    res = min(res, dfs(cur + 1, a, b + l[cur], c) + 10)
    res = min(res, dfs(cur + 1, a, b, c + l[cur]) + 10)
    res = min(res, dfs(cur + 1, a + l[cur] - 1, b, c) + 9)
    res = min(res, dfs(cur + 1, a, b + l[cur] - 1, c) + 9)
    res = min(res, dfs(cur + 1, a, b, c + l[cur] - 1) + 9)
    res = min(res, dfs(cur + 1, a + l[cur] - 2, b, c) + 8)
    res = min(res, dfs(cur + 1, a, b + l[cur] - 2, c) + 8)
    res = min(res, dfs(cur + 1, a, b, c + l[cur] - 2) + 8)
    return res

print(dfs(0, 0, 0, 0))
