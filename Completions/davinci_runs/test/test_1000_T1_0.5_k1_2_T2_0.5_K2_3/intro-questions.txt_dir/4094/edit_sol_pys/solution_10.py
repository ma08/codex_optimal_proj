import math

import sys

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = [0 for i in range(n)]
    for i in range(m):
        l, r = map(int, input().split())
        b[l-1] += 1
        b[r] -= 1
    c = [0 for i in range(n)]
    c[0] = b[0]
    for i in range(1, n):
        c[i] = c[i-1] + b[i]
    c.sort()
    a.sort()
    ans = 0
    for i in range(n):
        ans += c[i] * a[i]
    print(ans)

if __name__ == '__main__':
    main()
