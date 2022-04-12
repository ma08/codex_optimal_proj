
import math
import sys

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()

    days = 0
    for i in range(n-1):
        m -= a[i]
        days += 1
        if m <= a[-1]:
            break
    print(days + math.ceil(m / a[-1]))


if __name__ == "__main__":
    main()
