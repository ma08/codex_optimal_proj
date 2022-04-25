import math

def gcd(a, b):
    if b == 0:
        return a
    while b != 0:
        r = a % b
        a, b = b, a % b
    return b

a, b, k = map(int, input().split())

g = gcd(a, b)

divisors = []
for i in range(1, int(math.sqrt(g)) + 1):
    if g % i == 0:
        divisors.append(i)
        if i != g // i:
            divisors.append(g // i)

divisors.sort(reverse=True)

print(divisors[k - 1])
