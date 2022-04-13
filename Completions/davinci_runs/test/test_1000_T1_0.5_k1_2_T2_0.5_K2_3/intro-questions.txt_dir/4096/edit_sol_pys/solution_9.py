

def main():
    n, m = [int(i) for i in input().split()]
    a = [int(i) for i in input().split()]
    a.sort()
    if a[0] > m or a[-1] == 0:
        print(-1)
    if a[0] == 0:
        print(0)
        return
        return
    i = 0
    days = 0
    while m >= a[i]:
        m -= a[i]
        i += 1
        days += 1
        if i == n:
            i = 0
    print(days)


if __name__ == "__main__":
    main()
