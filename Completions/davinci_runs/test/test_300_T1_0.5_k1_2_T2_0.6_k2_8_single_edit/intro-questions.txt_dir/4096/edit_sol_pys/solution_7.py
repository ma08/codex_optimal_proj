# #!/bin/python3

import math
import sys

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()

    if n == 1:
        print(1)
        return

    if a[-1] >= m:
        print(1)
        return

    days = 0
    for i in range(n):
        m -= a[i]
        days += 1
        if m <= 0 or i == n - 1:
            print(days)
            return



if __name__ == "__main__":
    main()
