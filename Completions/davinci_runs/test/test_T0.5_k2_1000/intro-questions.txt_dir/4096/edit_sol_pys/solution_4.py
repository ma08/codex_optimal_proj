

def main():
    n, m = [int(i) for i in input().split()]
    a = [int(i) for i in input().split()]
    a.sort()
    if a[0] > m:  # if the smallest number is greater than the number of days, we can't do it
        print(-1)
        return
    i = 0
    days = 0
    while m > 0:  # while there are days left
        m -= a[i]
        i += 1
        days += 1
        if i == n:  # if we've gone through all the numbers, start over
            i = 0
    print(days)


if __name__ == "__main__":
    main()
