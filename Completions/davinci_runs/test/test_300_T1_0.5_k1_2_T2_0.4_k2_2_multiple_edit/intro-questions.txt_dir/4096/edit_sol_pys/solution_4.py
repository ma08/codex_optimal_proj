
import math
import sys

def main():
    n, m = map(int, input().split()) # n = number of days, m = max number
    a = list(map(int, input().split()))
    a.sort() # sort the list

    if a[-1] >= m:
        print(1)
        return

    days = 0
    for i in range(n):
        m -= a[i]
        days += 1
        if m <= 0:
            print(days)
            return

    if m % a[-1] == 0:
        print(days + math.ceil(m / a[-1]))
    else:
        print(-1)


if __name__ == "__main__":
    main()
