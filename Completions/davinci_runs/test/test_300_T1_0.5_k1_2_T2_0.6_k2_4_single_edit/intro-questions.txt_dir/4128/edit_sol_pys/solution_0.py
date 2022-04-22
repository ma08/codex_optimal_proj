from sys import stdin
from collections import namedtuple


def solve(n):
    return n // 2


if __name__ == "__main__":
    t = int(stdin.readline())
    for i in range(t):
        n = int(stdin.readline())
        print(solve(n))
