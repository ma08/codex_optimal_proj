


def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    a.reverse()
    days = 0
    pages = 0
    for i in range(n):
        pages += max(0, a[i] - i)
        if pages >= m:
            days += 1
            break
    if pages >= m:
        print(days)
    else:
        print(-1)


if __name__ == '__main__':
    main()