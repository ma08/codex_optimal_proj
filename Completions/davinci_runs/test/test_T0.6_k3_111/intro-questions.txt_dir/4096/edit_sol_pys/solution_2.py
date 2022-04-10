


def solve(n, m, a):
    a.sort(reverse=True)
    if a[0] >= m:
        return -1

    s = 0
    for k in range(n):
        if s >= m:
            return k
        s += a[k] - k

    if s >= m:
        return n
    else:
        return -1


def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    print(solve(n, m, a))


if __name__ == '__main__':
    main()
