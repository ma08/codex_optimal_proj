
import math
import sys

def main():
    n, m = map(int, input().split())  # n is number of days, m is number of pages
    a = list(map(int, input().split()))  # a is a list of pages per day
    a.sort()  # sort the list

    if a[-1] >= m:  # if max number of pages is greater than or equal to m
        print(1)
        return

    days = 0  # number of days
    for i in range(n):
        m -= a[i]  # decrease m by the number of pages
        days += 1  # increase number of days by 1
        if m <= 0:  # if the number of pages left is less than or equal to 0
            print(days)
            return

    if m % a[-1] == 0:
        print(days + math.ceil(m / a[-1]))
    else:
        print(-1)


if __name__ == "__main__":
    main()
