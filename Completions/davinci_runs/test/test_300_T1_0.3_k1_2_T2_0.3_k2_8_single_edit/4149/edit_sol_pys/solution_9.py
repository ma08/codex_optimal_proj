import math

n = int(input())
b = list(map(int, input().split()))

a = []

for i in range(n):
    a.append(b[i] // b[n + i])

print(*a)
