

def main():
    n, m = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    b.sort()
    if b[0] > m or m < n:
        print(-1)
        return
    i = 0
    days = 0
    while m > 0:
        m -= b[i]
        i += 1
        days += 1
        if i == n:
            i = 0
    print(days)


if __name__ == "__main__":
    main()
