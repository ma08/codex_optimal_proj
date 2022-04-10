


def solve(n, m):
    if n == 1:
        return 0
    if n == 2:
        return m
    if n == 3:
        return m - 1
    if n == 4:
        return m - 2
    if n % 2 == 0:
        return m - n // 2 + 1
    else:
        return m - n // 2

T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    print(solve(n, m))