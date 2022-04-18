from math import sqrt

n = int(input())
a = list(map(int, input().split()))

gcd = a[0]
for i in range(1, n):
    gcd = Gcd(gcd, a[i])

divisors = []

for i in range(1, int(sqrt(gcd)) + 1):
    if gcd % i == 0:
        divisors.append(i)
        if i != gcd // i:
            divisors.append(gcd // i)

print(len(divisors))
