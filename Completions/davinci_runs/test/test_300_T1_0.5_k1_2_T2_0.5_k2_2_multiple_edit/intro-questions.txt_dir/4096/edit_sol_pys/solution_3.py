
import math
import sys

def main():
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()

    if arr[-1] >= m:
        print(1)
        return

    days = 0
    for i in range(n):
        m -= arr[i]
        days += 1
        if m <= 0:
            print(days)
            return

    if m % arr[-1] == 0:
        print(days + math.ceil(m / arr[-1]))
    else:
        print(-1)


if __name__ == "__main__":
    main()
