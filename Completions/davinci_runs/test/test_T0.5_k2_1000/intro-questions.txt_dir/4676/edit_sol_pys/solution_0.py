# -*- coding: utf-8 -*-

o = raw_input()
e = raw_input()

ans = ""
for i in range(len(o)):
    ans += o[i]
    if i < len(e):
        ans += e[i]

print(ans)
