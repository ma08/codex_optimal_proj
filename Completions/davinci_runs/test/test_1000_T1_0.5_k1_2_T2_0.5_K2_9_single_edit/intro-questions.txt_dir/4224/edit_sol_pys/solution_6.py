# coding: utf-8

N = int(input())
a = [int(x) for x in input().split()]

ans = 0

for x in a:
    while x % 2 == 0:
        x /= 2
        ans += 1

print(count)
