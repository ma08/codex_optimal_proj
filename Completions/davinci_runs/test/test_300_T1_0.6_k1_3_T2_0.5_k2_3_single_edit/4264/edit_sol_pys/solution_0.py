# coding: utf-8

n = int(input())

ans = 0
for i in range(1, n+1):
    num = len(str(i))
    if num % 2 != 0:
        ans += 1

print(ans)
