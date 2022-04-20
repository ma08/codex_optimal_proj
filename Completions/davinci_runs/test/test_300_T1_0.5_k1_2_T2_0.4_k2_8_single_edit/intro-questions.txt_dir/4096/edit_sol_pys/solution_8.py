

def main():
    n, m = [int(i) for i in input().split()]
    a = [int(i) for i in input().split()]
    a.sort()
    i = 0
    days = 0
    while m >= 0:
        if i == n:
            i = 0
        if a[i] > m:
            break
        else:
            m -= a[i]
            days += 1
        i += 1
    print(days)


if __name__ == "__main__":
    main()
