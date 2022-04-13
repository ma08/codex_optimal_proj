


n, k = map(int, input().split())

def solve(n, k):
    if k == 0:
        return 0
    elif k == 1:
        return (n + 1) / 2.0
    else:
        return (solve(n, k - 1) + n) / 2.0

print(solve(n, k))
