import math


n = int(input())
a = [int(i) for i in input().split()]

ans = 0

for i in range(n):
    ans += math.floor(a[i] / 2)
    a[i] %= 2

print(count)
