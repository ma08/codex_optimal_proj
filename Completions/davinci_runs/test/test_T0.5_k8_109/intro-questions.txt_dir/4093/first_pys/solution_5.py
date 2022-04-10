


def solve(n, m):
    if n == 1:
        return 0
    if m == 0:
        return n - 1

    return max(m - 1, n - m)


if __name__ == '__main__':
    n_tests = int(input())
    for _ in range(n_tests):
        n, m = map(int, input().split())
        print(solve(n, m))