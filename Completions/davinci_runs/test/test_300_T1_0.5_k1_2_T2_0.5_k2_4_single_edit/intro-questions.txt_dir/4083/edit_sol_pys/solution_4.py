

from collections import defaultdict

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# 解説を読んで実装
# 解説はこちら
# https://atcoder.jp/contests/abc140/submissions/9466997


def solve(N, M, A, B):
    ans = [0] * N
    ans[0] = A[0]
    for i in range(1, N):
        ans[i] = min(A[i], ans[i - 1] + A[i])

    for i in range(N - 2, -1, -1):
        ans[i] = min(ans[i], ans[i + 1] + A[i])

    for i in range(M):
        x, y = B[i]

        if x - 1 > 0:
            ans[x - 2] = min(ans[x - 2], y)

        if x - 1 < N - 1:
            ans[x] = min(ans[x], y)

    return sum(ans)

import sys

def main():
    N, M = map(int, readline().split())
    A = list(map(int, readline().split()))
    B = [list(map(int, readline().split())) for _ in range(M)]

    print(solve(N, M, A, B))


if __name__ == '__main__':
    main()
