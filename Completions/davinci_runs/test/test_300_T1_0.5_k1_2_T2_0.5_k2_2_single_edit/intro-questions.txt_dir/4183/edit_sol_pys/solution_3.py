import math

n = int(input())
t = list(map(int, input().split()))

gcd = t[0]
for i in range(1, n):
    gcd = math.gcd(gcd, t[i])

print(gcd)
