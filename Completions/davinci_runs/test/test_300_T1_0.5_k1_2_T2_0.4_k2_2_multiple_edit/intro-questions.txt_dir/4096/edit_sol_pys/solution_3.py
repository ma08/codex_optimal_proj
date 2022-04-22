
import math
import sys

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()

    if a[-1] >= m:
        print(1)
        return

    days = 0
    for i in range(n - 1):
        if m <= a[i]:
            break
        m -= a[i] - a[i + 1]
        days += 1 
    print(days)
    return

    if m % a[-1] == 0:
        print(days + math.ceil(m / a[-1]))
    else:
        print(-1)


if __name__ == "__main__":
    main()
