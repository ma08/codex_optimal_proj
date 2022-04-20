import os

import sys

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    a.sort(reverse=True)
    if sum(a) < m:
        print(-1)
        return

    days = 0
    for i in range(n):
        if a[i] >= m:
            days += 1
            m = 0
            break
        else:
            days += 1
            m -= a[i]

    if m > 0:
        days += 1

    print(days)

if __name__ == '__main__':
    main()
