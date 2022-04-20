

def main():
    n, m = [int(i) for i in input().split()]
    a = [int(i) for i in input().split()]
    a.sort(reverse=True)
    i = n - 1
    days = 0
    while m > 0:
        m -= a[i]
        i -= 1
        days += 1
        if i == -1:
            i = n - 1
    print(days)


if __name__ == "__main__":
    main()
