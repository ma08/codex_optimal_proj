import sys
sys.setrecursionlimit(10**6)


def solve(n, h, l, r, a):
    if n == 0:
        return 0
    else:
        return max(solve(n - 1, a[n - 1], l, r, a) + (l <= a[n - 1] <= r), solve(n - 1, (a[n - 1] + 1) % h, l, r, a) + (l <= (a[n - 1] + 1) % h <= r), solve(n - 1, (a[n - 1] - 1) % h, l, r, a) + (l <= (a[n - 1] - 1) % h <= r))


def main():
    n, h, l, r = map(int, input().split())
    a = list(map(int, input().split()))
    print(solve(n, 0, l, r, a))


if __name__ == "__main__":
    main()
