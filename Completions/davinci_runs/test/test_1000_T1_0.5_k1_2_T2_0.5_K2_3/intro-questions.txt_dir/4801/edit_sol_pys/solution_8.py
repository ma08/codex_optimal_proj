# https://codeforces.com/contest/1144/problem/A


import sys

input = sys.stdin.readline

n, k = map(int, input().split())
a = list(map(int, input().split()))

if k == 1:
    print(n)
elif k == 2:
    print(n + 1)
else:
    i = 0
    while i < n:
        j = i
        while j < n and a[j] == a[i]:
            j += 1
        if j - i >= k:
            i = j
        else:
            a.insert(i, a[i])
            i += 1

    if a[-1] == a[-2]:
        a.append(a[-1])

    if a[0] == a[1]:
        a.insert(0, a[0])

    if len(a) <= 2 * k:
        print(2)
    else:
        print(len(a))
    print(*a)
