

import sys

def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    a.sort()
    d = {}
    for i in a:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    l = len(d)
    if l == 1:
        print(1)
        return
    m = max(d.values())
    if m == n:
        print(l)
        return
    if m == n - 1:
        print(l - 1)
        return
    if m == n - 2:
        if l == 2:
            print(1)
            return
        else:
            print(l - 2)
            return
    print(0)

if __name__ == '__main__':
    main()