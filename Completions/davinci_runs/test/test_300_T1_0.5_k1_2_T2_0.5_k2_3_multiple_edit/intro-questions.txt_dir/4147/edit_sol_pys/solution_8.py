# https://atcoder.jp/contests/abc142/tasks/abc142_d
# import sys
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# input = sys.stdin.buffer.readline
# from numba import njit
# from functools import lru_cache
# sys.setrecursionlimit(10 ** 7)

# @njit('(i8,i8[::1],i4[::1])', cache=True)
# def main():
#     @lru_cache(None)
#     def dfs():
#         return
#     return

# main()

# S = input()
# n = int(input())
# N, K = map(int, input().split())
# l = list(map(int, (input().split())))
# A = [[int(i) for i in input().split()] for _ in range(N)]


N, A, B, C = map(int, input().split())
ls = [int(input()) for _ in range(N)]

def dfs(cur, a, b, c):
    if a == A and b == B and c == C:
        return 0
    if cur == N:
        return float('inf')
    res = float('inf')
    res = min(res, dfs(cur + 1, a, b, c))
    res = min(res, dfs(cur + 1, a + ls[cur], b, c) + 10)
    res = min(res, dfs(cur + 1, a, b + ls[cur], c) + 10)
    res = min(res, dfs(cur + 1, a, b, c + ls[cur]) + 10)
    for i in range(1, ls[cur]):
        res = min(res, dfs(cur + 1, a + ls[cur] - i, b, c) + 10-i)
        res = min(res, dfs(cur + 1, a, b + ls[cur] - i, c) + 10-i)
        res = min(res, dfs(cur + 1, a, b, c + ls[cur] - i) + 10-i)
    return res

print(dfs(0, 0, 0, 0))
