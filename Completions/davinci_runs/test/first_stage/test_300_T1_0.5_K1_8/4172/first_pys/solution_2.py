

import sys

def main():
    n, k = map(int, sys.stdin.readline().split())
    a = map(int, sys.stdin.readline().split())
    mn = min(a)
    mx = max(a)
    if mn == mx:
        print 0
        return

    if k == n:
        print mx - mn
        return

    d = sorted([(a[i] - mn, i) for i in range(n)], reverse=True)
    c = 1
    for i in range(1, n):
        if d[i][0] == d[i - 1][0]:
            c += 1
        else:
            break
    o = c
    if c >= k:
        print d[c - 1][0]
        return

    c = 1
    for i in range(1, n):
        if d[i][0] == d[i - 1][0] and d[i][1] < d[i - 1][1]:
            c += 1
        else:
            break
    if c >= k:
        print d[c - 1][0]
        return

    mx = min(mx - mn, d[c - 1][0])
    for i in range(c, n):
        if d[i][0] > mx or d[i][0] <= d[c - 1][0]:
            break
        if d[i][1] > d[c - 1][1]:
            c += 1
        if c >= k:
            break
    if c >= k:
        print mx
        return

    print mx + (k - c)

if __name__ == '__main__':
    main()