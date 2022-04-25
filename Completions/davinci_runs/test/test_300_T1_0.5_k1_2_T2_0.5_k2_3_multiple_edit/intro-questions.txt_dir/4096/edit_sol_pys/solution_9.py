
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
    for i in range(n):
        m -= a[i]
        days += 1
        if m <= 0:
            print(days)
            return

    if m % a[-1] != 0:
        print(-1)
        return

    ans = days + math.ceil(m / a[-1])
    if ans < 0:
        print(ans)
    else:
        print(-1)


if __name__ == "__main__":
    main()
