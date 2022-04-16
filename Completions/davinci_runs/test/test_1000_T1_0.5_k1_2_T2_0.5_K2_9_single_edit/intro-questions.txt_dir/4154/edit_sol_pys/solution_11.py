


def solve(n, m, q):
    for i in range(q):
        l, r = map(int, input().split())
        print(n - m)


if __name__ == '__main__':
    n, m, q = map(int, input().split())
    solve(n, m, q)
