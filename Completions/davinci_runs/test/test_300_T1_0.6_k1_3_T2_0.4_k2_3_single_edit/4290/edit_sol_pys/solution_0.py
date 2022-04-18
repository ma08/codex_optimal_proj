

import sys

input = sys.stdin.readline

n, m = map(int, input().split())

if (n + m) % 2 == 0:
    print(2 ** (n + m) - 2 ** ((n + m) // 2))
else:
    print(2 ** (n + m))
