# coding: utf-8
import sys
sys.setrecursionlimit(1000000)


def solve(n, a):
    if n == 0:
        return 0

    b = [a[0]]
    for i in range(1, n):
        if a[i - 1] != a[i]:
            b.append(a[i])

    if len(b) == 1:
        return 0

    return solve(len(b), b) + 1



n = int(input())
a = list(map(int, input().split()))

ans = solve(n, a)

print(ans)
