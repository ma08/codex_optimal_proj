
import sys

sys.setrecursionlimit(1000000)

n = int(input())
a = list(map(int, input().split()))

def check(x):
    if x == 1:
        return True
    elif x % 2 == 0:
        return check(x // 2)
    else:
        return check(3 * x + 1)

def solve(i, n):
    if i == n:
        return 0
    else:
        if check(a[i]):
            return solve(i + 1, n)
        else:
            return max(solve(i + 1, n), solve(i + 1, n) + a[i])

max_rest = max(max_rest, rest)
print(max_rest)
