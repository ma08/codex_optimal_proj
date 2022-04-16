# coding: utf-8

n = int(input())
a = list(map(int, input().split()))

a_sum = 0
for i in range(n):
    a_sum += 1/a[i]

print(1/a_sum)
