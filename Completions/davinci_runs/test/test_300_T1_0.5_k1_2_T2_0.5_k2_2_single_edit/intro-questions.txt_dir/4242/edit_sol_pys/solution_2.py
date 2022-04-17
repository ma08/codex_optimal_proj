import math, fractions

def gcd(a,b):
    return fractions.gcd(a,b)

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
