# https://atcoder.jp/contests/abc085/tasks/abc085_c


def solve(n, y):
    for i in range(n + 1):
        for j in range(n + 1):
            k = n - i - j
            if k < 0:
                continue
            if 10000 * i + 5000 * j + 1000 * k == y:
                return i, j, k
    return -1, -1, -1


def main():
    n = int(input())
    y = int(input())
    print(*solve(n, y))


if __name__ == "__main__":
    main()
