
import math
import sys

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()

    if m <= a[-1]:
        print((m + a[-1] - 1) // a[-1])

    m -= a[-1] * (n - 1)

    days = 0
    while m > 0:
        m -= a[-1]
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
