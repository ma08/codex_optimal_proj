
import math
import sys

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()

    a.sort()

    days = 1
    for i in range(n):
        m -= a[i]
        days += 1
        if m < 0:
            print(days)
            return

    print(days + math.ceil(m / a[-1]))


if __name__ == "__main__":
    main()
