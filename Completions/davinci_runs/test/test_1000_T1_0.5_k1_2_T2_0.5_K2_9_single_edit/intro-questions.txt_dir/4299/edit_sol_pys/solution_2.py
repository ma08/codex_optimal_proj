# coding: utf-8


n, k = map(int, input().split())
r, s, p = map(int, input().split())
t = list(input())

ans = 0
for i in range(n):
    if i >= k and t[i] == t[i-k]:
        t[i] = "x"
    if t[i] == "r":
        ans += p
    elif t[i] == "s":
        ans += r
    elif t[i] == "p":
        ans += s

print(ans)
