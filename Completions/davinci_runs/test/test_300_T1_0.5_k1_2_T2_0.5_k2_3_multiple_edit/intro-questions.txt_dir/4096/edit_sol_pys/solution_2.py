def main():
    n, m = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    a.sort(reverse=True)
    if a[-1] > m:
        print(-1)
        return
    i = 0
    days = 0
    while m >= 0:
        m -= a[i % n]
        i += 1
        days += 1
    print(days)


if __name__ == "__main__":
    main()
