
def main():
    n, m = [int(i) for i in input().split()] # n is number of books, m is the number of days
    a = [int(i) for i in input().split()]
    a.sort()
    if a[0] > m: # if the first book is already heavier than the number of days, it is impossible
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
