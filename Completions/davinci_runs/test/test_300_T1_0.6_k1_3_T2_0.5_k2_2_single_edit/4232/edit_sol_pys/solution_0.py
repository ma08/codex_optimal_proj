
from sys import stdin


def solve():
    n, k = map(int, stdin.readline().split())
    a = sorted(map(int, stdin.readline().split()))

    print(a[k - 1] if k else -1)


if __name__ == "__main__":
    solve()
