
def solve(N, d):
    d.sort()

    l = sum(d[:N // 2])
    r = sum(d[N // 2:])

    return d[-1] - d[0] + 1 if l == r else 0


def main():
    N = int(input())
    d = list(map(int, input().split()))

    print(solve(N, d))


if __name__ == '__main__':
    main()
