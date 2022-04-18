

def main():
    n, m = [int(i) for i in input().split()]
    a = [int(i) for i in input().split()]
    a = sorted(a)
    i = 0
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
