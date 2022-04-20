
import sys


def solve(k, n, a, b):
    if n * b > k:
        return -1
    else:
        return k - n * b


q = int(input())

for _ in range(q):
    k, n, a, b = map(int, sys.stdin.readline().rstrip().split())

    if n * b > k:
        print(-1)
    else:
        print(k - n * b)
