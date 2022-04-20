

import sys

def main():
    n, m = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    a.sort(reverse=True)
    if sum(a) < m:
        print(-1)
        return
    d = 0
    for i in range(n):
        if a[i] >= m:
            d += 1
            m = 0
            break
        m -= a[i]
        d += 1
    if m > 0:
        d += (m + d - 1) // d
    print(d)

if __name__ == "__main__":
    main()