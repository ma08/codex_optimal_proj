# https://atcoder.jp/contests/abc085/tasks/abc085_c


def solve(n, y):
    for i in range(n + 1):
        for j in range(n + 1 - i):
            k = n - i - j
            if 10000 * i + 5000 * j + 1000 * k == y:
                return i, j, k
    return -1, -1, -1


def main():
    n = int(input())
    q = list(map(int, input().split()))
    print(*solve(n, q))


if __name__ == "__main__":
    main()
