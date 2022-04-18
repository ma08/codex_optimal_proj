# coding=utf-8

k = int(input())
n = int(input())
for i in range(n):
    t, z = input().split()
    t = int(t)
    if t > 210:
        break
    if z == "T":
        k = (k + 1) % 8 + 1
    if z == "N":
        k = (k - 1) % 8 + 1
print(k)
