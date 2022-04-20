


def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    if max(a) * n < m:
        print(-1)
        return

    a.sort(reverse=True)
    res = 0
    days = 0
    for i in range(n):
        days += 1
        res += a[i] - days + 1
        if res >= m:
            print(days)
            return

    print(-1)


if __name__ == "__main__":
    main()