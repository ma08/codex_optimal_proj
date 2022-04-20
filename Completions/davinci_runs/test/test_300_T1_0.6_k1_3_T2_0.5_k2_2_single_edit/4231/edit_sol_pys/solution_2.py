from math import ceil


n, a, b = map(int, input().split())

print(ceil(n/(a+b))*a)
