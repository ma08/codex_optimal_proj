import heapq

N, A, B, C = map(int, input().split())
ls = [int(input()) for _ in range(N)]

def dfs(cur, a, b, c):
    if cur == N:
        return float('inf')
    if cur == N - 1:
        if a == 0 or b == 0 or c == 0:
            return float('inf')
        if a == A and b == B and c == C:
            return 0
        else:
            return abs(a - A) + abs(b - B) + abs(c - C) - 30
    return min(
        dfs(cur + 1, a + ls[cur], b, c) + 10,
        dfs(cur + 1, a, b + ls[cur], c) + 10,
        dfs(cur + 1, a, b, c + ls[cur]) + 10,
        dfs(cur + 1, a + ls[cur] - 1, b, c) + 9,
        dfs(cur + 1, a, b + ls[cur] - 1, c) + 9,
        dfs(cur + 1, a, b, c + ls[cur] - 1) + 9,
        dfs(cur + 1, a + ls[cur] - 2, b, c) + 8,
        dfs(cur + 1, a, b + ls[cur] - 2, c) + 8,
        dfs(cur + 1, a, b, c + ls[cur] - 2) + 8,
        dfs(cur + 1, a, b, c) + 0,
    )

print(dfs(0, 0, 0, 0))
