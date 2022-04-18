
from itertools import accumulate


def solve(n, q):
    p = list(accumulate(q))
    if p[-1] != n - 1:
        return [-1]
    return p + [1]


def main():
    n = int(input())
    q = list(map(int, input().split()))
    print(*solve(n, q))


if __name__ == "__main__":
    main()
