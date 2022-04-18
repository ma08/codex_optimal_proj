
def main():
    n, m = [int(i) for i in input().split()]
    a = [int(i) for i in input().split()][:n]
    a.sort()
    if a[0] > m or n > m:
        print(-1)
        return
    i = 0
    days = 0
    while m > 0 and i < n:
        if a[i] <= m:
            m -= a[i]
            days += 1
        i += 1
    if m > 0:
        print(-1)
    else:
        print(days)


if __name__ == "__main__":
    main()
