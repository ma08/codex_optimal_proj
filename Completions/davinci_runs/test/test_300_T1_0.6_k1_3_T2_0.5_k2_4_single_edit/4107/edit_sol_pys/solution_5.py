import sys
sys.setrecursionlimit(10 ** 6)

n, k = map(int, input().split())
s = input()


def solve(i, cnt):
    if i >= n:
        return cnt
    if s[i] == '1':
        return solve(i + 1, cnt)
    if i - k >= 0 and s[i - k] == '1':
        return solve(i + 1, cnt)
    if i + k < n and s[i + k] == '1':
        return solve(i + 1, cnt)
    return solve(i + 1, cnt + 1)


print(solve(0, 0))
