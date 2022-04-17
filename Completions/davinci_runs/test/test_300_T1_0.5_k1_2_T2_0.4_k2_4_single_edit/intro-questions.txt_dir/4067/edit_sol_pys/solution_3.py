#!/usr/bin/env python3

n = int(input())
s = input()

# s = '120110'
# n = len(s)

a = [0, 0, 0]
for i in range(n):
    a[int(s[i])] += 1

# print(a)

if a[1] == a[2]:
    print(s)
else:
    k = a[1] - a[2]
    if k < 0:
        k = -k
    r = k // 3
    if k % 3 != 0:
        r += 1
    # print(r)
    a[1] -= r
    a[2] += r
    # print(a)
    ans = ''
    for i in range(n):
        if a[0] > 0:
            ans += '0'
            a[0] -= 1
        elif a[1] > 0:
            ans += '1'
            a[1] -= 1
        elif a[2] > 0:
            ans += '2'
            a[2] -= 1
    print(ans)
