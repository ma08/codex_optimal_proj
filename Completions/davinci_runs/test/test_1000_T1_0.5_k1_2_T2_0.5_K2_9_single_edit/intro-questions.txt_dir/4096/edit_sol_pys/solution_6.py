
import math
import sys

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))  # map(int, input().split())
    a.sort()

    a = [a[i] for i in range(n) if a[i] < m]
    a.sort()
    n = len(a)

    days = 0
    while m > 0:
        for i in range(n):
            m -= a[i]
            days += 1
            if m <= 0:
                print(days)
                return

    print(-1)


if __name__ == "__main__":
    main()
