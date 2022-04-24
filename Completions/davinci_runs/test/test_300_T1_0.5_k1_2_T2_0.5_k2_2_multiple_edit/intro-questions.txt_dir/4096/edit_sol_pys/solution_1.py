

def main():
    n, m = [int(i) for i in input().split()]  # input the number of apples and the number of days
    a = [int(i) for i in input().split()]
    a.sort()  # sort the list of apples
    if a[0] > m:  # if the smallest apple is more than the number of days, then it is impossible to eat all the apples
        print(-1)
        return
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
