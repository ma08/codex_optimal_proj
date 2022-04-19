def main():
    n, m = [int(i) for i in input().split()]
    a = [int(i) for i in input().split()]
    a.sort()
    i = 0
    days = 0
    while True:
        if m > a[i]:
            m -= a[i]
            i += 1
            days += 1
        else:
            days += 1
            break
        if i == n:
            i = 0
    print(days)


if __name__ == "__main__":
    main()
