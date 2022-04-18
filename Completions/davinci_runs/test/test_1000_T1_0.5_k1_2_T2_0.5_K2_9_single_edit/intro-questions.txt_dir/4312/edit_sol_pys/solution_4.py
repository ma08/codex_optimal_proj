# -*- coding: utf-8 -*-

N = int(input())
a_list = list(map(int, input().split()))

ans = 0
for i in range(N):
    tmp = 0
    while a_list[i] % 2 == 0:
        a_list[i] //= 2
        tmp += 1
    ans += tmp

print(ans)
