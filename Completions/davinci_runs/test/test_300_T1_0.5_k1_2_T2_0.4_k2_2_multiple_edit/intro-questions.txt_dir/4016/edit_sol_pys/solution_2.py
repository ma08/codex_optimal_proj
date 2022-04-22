# coding: utf-8

n, k = map(int, input().split())
t = input()

ans = ""
for i in range(n):
    ans += t[(i + k) % n]

print(ans)
