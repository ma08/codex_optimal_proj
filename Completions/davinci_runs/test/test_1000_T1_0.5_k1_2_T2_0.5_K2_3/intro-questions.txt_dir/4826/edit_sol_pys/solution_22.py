import sys

sys.setrecursionlimit(10 ** 7)


def solve(a, b, c, d):
    return "Yes" if a <= c <= b or a <= d <= b or c <= a <= d or c <= b <= d else "No"


if __name__ == "__main__":
    a, b, c, d = map(int, input().split())
    print(solve(a, b, c, d))
