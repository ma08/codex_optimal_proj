

def main():
    n, m = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    a.sort()
    a.reverse()

    days = 0
    pages = 0
    for i in range(n):
        pages += a[i] - i
        if pages >= m:
            days += 1
            pages = 0

    if pages == 0:
        print(days)
    else:
        print(-1)


if __name__ == "__main__":
    main()