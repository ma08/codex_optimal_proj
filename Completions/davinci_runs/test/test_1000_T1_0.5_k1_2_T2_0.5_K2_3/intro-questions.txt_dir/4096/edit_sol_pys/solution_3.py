
import math
import sys

def main():
    n, m = map(int, input().split())
    as_ = list(map(int, input().split()))
    as_.sort()

    if as_[-1] >= m:
        print(1)
        return

    days = 0
    for i in range(n):
        m -= as_[i]
        days += 1
        if m <= 0:
            print(days)
            return

    if m % as_[-1] == 0:
        print(days + math.ceil(m / as_[-1]))
    else:
        print(-1)


if __name__ == "__main__":
    main()
