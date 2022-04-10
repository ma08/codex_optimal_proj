

import re

n = int(input())
s = input()
t = input()

if n == 1:
    print("YES")
    print("abc")
    exit(0)

if s[0] == t[0]:
    print("NO")
    exit(0)

print("YES")

res = ""

if s[0] == s[1]:
    res = s[0] * n
    res += t[0] * n
    res += t[1] * n
else:
    if t[0] == t[1]:
        res = s[0] * n
        res += s[1] * n
        res += t[0] * n
    else:
        res = s[0] * n
        res += s[1] * n
        res += t[0] * n
        res += t[1] * n

print(res)