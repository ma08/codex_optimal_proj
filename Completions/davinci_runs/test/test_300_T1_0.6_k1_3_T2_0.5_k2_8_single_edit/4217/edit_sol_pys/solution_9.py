#
# https://codeforces.com/problemset/problem/1257/A
#
#
#
#


def solve(n, x, a, b):
    answer = abs(a - b) + x
    if a > b:
        answer -= min(a - 1, n - b)
    else:
        answer -= min(b - 1, n - a)
    return answer


q = int(input())

for _ in range(q):
    n, x, a, b = [int(n) for n in input().split()]
    print(solve(n, x, a, b))
