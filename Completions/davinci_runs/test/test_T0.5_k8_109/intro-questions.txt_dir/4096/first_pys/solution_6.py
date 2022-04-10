


def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    a.sort(reverse=True)
    days = 0
    pages = 0
    for x in a:
        days += 1
        pages += x - days + 1
        if pages < 0:
            print(-1)
            return

    if pages < m:
        print(-1)
    else:
        print(days)


if __name__ == "__main__":
    main()