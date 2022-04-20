import math

n = int(input())
divisors = [int(i) for i in input().split() if int(i) != 1]

divisors.sort()

x = divisors[0]
y = divisors[-1]

print(math.gcd(x, y))
