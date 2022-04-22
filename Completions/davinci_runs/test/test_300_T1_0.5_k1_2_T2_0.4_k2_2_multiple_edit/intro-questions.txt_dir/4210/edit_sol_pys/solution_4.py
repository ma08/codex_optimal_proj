"""
https://atcoder.jp/contests/abc065/tasks/arc076_c
"""

n, m = map(int, input().split())

if abs(n - m) > 1:
    print(0)
    exit()

def fact(n):
    if n == 0:
        return 1
    return n * fact(n - 1)

if n == m:
    print(2 * fact(n) * fact(m) % (10**9 + 7))
else:
    print(fact(n) * fact(m) % (10**9 + 7))
