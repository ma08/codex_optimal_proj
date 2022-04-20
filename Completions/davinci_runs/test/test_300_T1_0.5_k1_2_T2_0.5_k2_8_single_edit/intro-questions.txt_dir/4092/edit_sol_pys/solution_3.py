
import sys

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    a.sort()
    c.sort()
    for i in b:
        l = lower_bound(a, i)
        r = upper_bound(c, i)
        print(l + r, end=' ')

def lower_bound(a, x):
    l = -1
    r = len(a)
    while r - l > 1:
        m = (l + r) // 2
        if a[m] >= x:
            r = m
        else:
            l = m
    return r

def upper_bound(a, x):
    l = -1
    r = len(a)
    while r - l > 1:
        m = (l + r) // 2
        if a[m] > x:
            r = m
        else:
            l = m
    return len(a) - r

if __name__ == '__main__':
    main()
