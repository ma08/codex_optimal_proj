def solve(n, m, k, A):
    pass


def main():
    n, m, k = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(n)]

    print(solve(n, m, k, A))


if __name__ == '__main__':
    main()
