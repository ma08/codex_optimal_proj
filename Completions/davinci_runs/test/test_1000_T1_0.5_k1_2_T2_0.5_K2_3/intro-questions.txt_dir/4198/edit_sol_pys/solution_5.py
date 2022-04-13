# coding: utf-8

a, b, x = map(int, input().split())

if a + b > x:
    print(0)
    exit()

k = (x - b) / a
l = len(str(k))

if a * k + b * l > x:
    k -= 10 ** (l - 1)

print(k)
