import math

def gcd(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        a, b = b, a % b
    return a

a, b, k = map(int, input().split()) # input a, b, k

g = gcd(a, b) # Greatest Common Divisor

divisors = [] # divisors of g
for i in range(1, int(math.sqrt(g)) + 1):
    if g % i == 0:
        divisors.append(i)
        if i != g // i:
            divisors.append(g // i)

divisors.sort(reverse=True) # sort divisors of g in descending order

print(divisors[k - 1])
