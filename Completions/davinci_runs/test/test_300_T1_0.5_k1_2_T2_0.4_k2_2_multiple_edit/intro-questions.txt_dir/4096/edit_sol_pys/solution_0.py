

def main():
    n, m = [int(i) for i in input().split()]  # n - number of pages, m - number of minutes, a - list of pages
    a = [int(i) for i in input().split()]
    a.sort()  # sort list of pages
    if a[0] > m:  # if the first page is more than the number of minutes, then there is no solution
        print(-1)
        return
    i = 0  # number of pages
    days = 0  # number of days
    while m > 0:  # while there are minutes
        m -= a[i]  # subtract minutes
        i += 1  # increase the number of pages
        days += 1  # increase the number of days
        if i == n:  # if all the pages have been read, then start from the beginning
            i = 0  # start from the beginning
    print(days)  # print the number of days


if __name__ == "__main__":
    main()
