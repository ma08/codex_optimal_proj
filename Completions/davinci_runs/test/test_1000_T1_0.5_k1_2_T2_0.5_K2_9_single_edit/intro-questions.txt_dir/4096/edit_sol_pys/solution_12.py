
def main():
    n, m = [int(i) for i in input().split()]
    a = [int(i) for i in input().split()]
    a.sort()
    if a[0] > m:
        print(-1)
        return
    i = 0 # index of a's elements
    days = 0
    while m > 0:
        m -= a[i]
        i += 1
        days += 1
        if i == n:
            i = 0
    print(days)


if __name__ == "__main__":
    main()
