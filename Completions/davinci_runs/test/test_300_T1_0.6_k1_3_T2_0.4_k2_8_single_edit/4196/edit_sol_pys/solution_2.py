import math


n = int(input())
a = list(map(int, input().split()))

a.sort()
print(a[0]*a[n-1]//math.gcd(a[0], a[n-1]))
