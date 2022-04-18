

def main():
    n, m = [int(i) for i in input().split()]
    a = [int(i) for i in input().split()]
    a.sort()
    i = 0
    if a[0] > m:
        days = -1
    else:
        if m % a[0] == 0:
            days = m // a[0]
        else:
            days = m // a[0] + 1
    days = 0
    while m > 0:
        m -= a[i]
        i += 1
        if i == n:
            i = 0
    print(days)


if __name__ == "__main__":
    main()
