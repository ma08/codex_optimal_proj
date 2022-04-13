

def main():
    n, m = [int(i) for i in input().split()]
    a = [int(i) for i in input().split()]  # list of prices
    a.sort()  # sort prices
    if a[0] > m:  # if the minimum price is greater than m, then it is not possible to solve this task
        print(-1)
        return
    i = 0
    days = 0
    while m > 0:  # while there is money left in the wallet
        m -= a[i]
        i += 1
        days += 1
        if i == n:
            i = 0
    print(days)


if __name__ == "__main__":
    main()
