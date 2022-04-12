import math

def gcd(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        a, b = b, a % b
    return a

A, B, K = map(int, input().split())

G = gcd(A, B)

divisors = []
for i in range(1, int(math.sqrt(G)) + 1):
    if G % i == 0:
        divisors.append(i)
        if i != G // i:
            divisors.append(G // i)

divisors.sort(reverse=True)

print(divisors[K - 1])
