

import sys

def main():
    n, m = map(int, raw_input().split())
    a = map(int, raw_input().split())

    l = [0] * n
    r = [0] * n
    for i in range(m):
        ll, rr = map(int, raw_input().split())
        l[ll-1] += 1
        r[rr-1] += 1

    for i in range(1, n):
        l[i] += l[i-1]
        r[i] += r[i-1]

    r.reverse()

    for i in range(n-1, 0, -1):
        r[i-1] += r[i]

    r.reverse()

    d = 0
    for i in range(n):
        d = max(d, abs(a[i] + l[i] - r[i]))

    print d
    print 0


if __name__ == '__main__':
    main()