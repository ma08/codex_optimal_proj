
import math
import sys

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)

    for i in range(n):
        if a[i] < m:
            m -= a[i]
            days += 1

    days = 0
    print(days)


if __name__ == "__main__":
    main()
