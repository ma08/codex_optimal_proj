

import sys

def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    d = {}
    for i in range(n):
        if a[i] in d:
            d[a[i]].append(i)
        else:
            d[a[i]] = [i]
    m = {}
    for i in range(n):
        if a[i] not in m:
            m[a[i]] = 0
        if a[i]-1 in m:
            m[a[i]] = max(m[a[i]], m[a[i]-1]+1)
        if a[i]+1 in m:
            m[a[i]] = max(m[a[i]], m[a[i]+1]+1)
        if a[i] in d and len(d[a[i]]) > 1:
            m[a[i]] = max(m[a[i]], m[a[i]]+1)
    print(max(m.values()))

if __name__ == '__main__':
    main()